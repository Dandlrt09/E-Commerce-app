import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="E-commerce Olist Analysis",
    page_icon="🛒",
    layout="wide"
)

# ── Cargar datos ──
@st.cache_data
def cargar_datos():
    orders = pd.read_csv('olist_orders.csv')
    items = pd.read_csv('olist_items.csv')
    products = pd.read_csv('olist_products.csv')
    
    # Merge para obtener el dataset completo
    df = pd.merge(items, orders, on='order_id', how='inner')
    df = pd.merge(df, products, on='product_id', how='inner')
    
    # Limpiar y preparar datos
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    return df

# Cargar datos
df = cargar_datos()

# Título principal
st.title("🛒 Análisis de Ventas - E-commerce Olist")
st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Datos", "📈 Análisis", "📊 Visualizaciones", "ℹ️ Sobre el proyecto"])

# Tab 1: Datos
with tab1:
    st.header("📊 Exploración del Dataset")
    st.write("Acá vas a conocer los datos de **Olist**, la mayor tienda por departamentos de Brasil.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Vista de los datos")
        st.caption("Mostrando las primeras 10 filas del dataset:")
        st.dataframe(df.head(10), width='stretch')
        st.success(f"**Total de pedidos:** {df['order_id'].nunique():,} pedidos únicos")
        st.info(f"**Total de ítems:** {len(df):,} productos vendidos")
        st.warning(f"**Total de productos:** {df['product_id'].nunique():,} productos únicos")
    
    with col2:
        st.subheader("Estadísticas clave")
        st.caption("Resumen de precios e ítems:")
        st.dataframe(df[['price', 'freight_value']].describe(), width='stretch')
        
        st.caption("""
        **💡 Sobre los datos:**
        - Precio promedio: R$ {df['price'].mean():.2f}
        - Pedido más caro: R$ {df['price'].max():.2f}
        - Producto más vendido: {df['product_id'].value_counts().idxmax()}
        """)
    
    st.markdown("---")
    
    st.subheader("📋 ¿Qué variables tenemos?")
    st.write("El dataset combinado contiene información de pedidos, ítems y productos:")
    
    variables_info = pd.DataFrame({
        'Variable': ['order_id', 'customer_id', 'order_status', 'price', 'freight_value', 
                    'product_id', 'product_category_name', 'product_weight_g'],
        '¿Qué es?': [
            'ID único del pedido',
            'ID único del cliente',
            'Estado del pedido (delivered, shipped, etc.)',
            'Precio del producto en Reales (R$)',
            'Costo de envío en Reales',
            'ID único del producto',
            'Categoría del producto',
            'Peso del producto en gramos'
        ],
        'Tipo': ['Categórica', 'Categórica', 'Categórica', 'Numérico', 'Numérico', 
                  'Categórica', 'Categórica', 'Numérico']
    })
    
    st.dataframe(variables_info, width='stretch', hide_index=True)

# Tab 2: Análisis
with tab2:
    st.header("📈 Análisis de Ventas")
    st.write("Insights clave sobre el comportamiento de ventas de Olist.")
    
    # Top categorías por ingresos
    st.subheader("🏆 Top 10 Categorías por Ingresos")
    
    top_categorias = df.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        top_categorias.plot(kind='bar', color='skyblue', ax=ax1)
        ax1.set_xlabel('Categoría del Producto')
        ax1.set_ylabel('Ingresos Totales (R$)')
        ax1.set_title('Top 10 Categorías por Ingresos')
        ax1.tick_params(axis='x', rotation=45, labelsize=8)
        plt.tight_layout()
        st.pyplot(fig1)
    
    with col2:
        st.write("**Categorías más rentables:**")
        for i, (cat, val) in enumerate(top_categorias.head(5).items(), 1):
            st.metric(f"#{i} {cat}", f"R$ {val:,.2f}")
    
    st.markdown("---")
    
    # Análisis de precios por categoría
    st.subheader("💰 Distribución de Precios por Categoría")
    
    top5_cats = top_categorias.head(5).index.tolist()
    df_top5 = df[df['product_category_name'].isin(top5_cats)]
    
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    df_top5.boxplot(column='price', by='product_category_name', ax=ax2, grid=False)
    ax2.set_xlabel('Categoría')
    ax2.set_ylabel('Precio (R$)')
    ax2.set_title('Distribución de Precios - Top 5 Categorías')
    ax2.tick_params(axis='x', labelsize=8)
    plt.tight_layout()
    st.pyplot(fig2)
    
    st.markdown("---")
    
    # Estado de los pedidos
    st.subheader("📦 Estatus de los Pedidos")
    
    order_status = df['order_status'].value_counts()
    
    col3, col4 = st.columns(2)
    
    with col3:
        fig3, ax3 = plt.subplots(figsize=(6, 4))
        order_status.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'orange', 'red', 'purple'], ax=ax3)
        ax3.set_ylabel('')
        ax3.set_title('Distribución de Estatus de Pedidos')
        st.pyplot(fig3)
    
    with col4:
        st.write("**Resumen de estatus:**")
        for status, count in order_status.items():
            pct = count / len(df) * 100
            st.write(f"- **{status}**: {count:,} ({pct:.1f}%)")

# Tab 3: Visualizaciones Interactivas (fixed matplotlib compatibility)
with tab3:
    st.header("📊 Visualizaciones Interactivas")
    st.write("Explora los datos con filtros y gráficos dinámicos.")
    
    # Filtros
    st.subheader("🎮 Filtros")
    col1, col2 = st.columns(2)
    
    with col1:
        categorias_disponibles = ['Todas'] + sorted(df['product_category_name'].unique().tolist())
        categoria_sel = st.selectbox("Selecciona una Categoría", categorias_disponibles)
    
    with col2:
        estados = ['Todos'] + sorted(df['order_status'].unique().tolist())
        estado_sel = st.selectbox("Selecciona Estatus de Pedido", estados)
    
    # Aplicar filtros
    df_filtrado = df.copy()
    if categoria_sel != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['product_category_name'] == categoria_sel]
    if estado_sel != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['order_status'] == estado_sel]
    
    st.info(f"Mostrando {len(df_filtrado):,} registros de {len(df):,} totales ({len(df_filtrado)/len(df)*100:.1f}%)")
    
    st.markdown("---")
    
    # Gráfico 1: Precios por categoría seleccionada
    if categoria_sel != 'Todas':
        st.subheader(f"📈 Distribución de Precios - {categoria_sel}")
        
        fig4, ax4 = plt.subplots(figsize=(8, 4))
        df_filtrado['price'].hist(bins=50, edgecolor='black', color='skyblue', alpha=0.7, ax=ax4)
        ax4.axvline(x=df_filtrado['price'].mean(), color='red', linestyle='--', 
                   label=f'Promedio: R$ {df_filtrado["price"].mean():.2f}')
        ax4.set_xlabel('Precio (R$)')
        ax4.set_ylabel('Cantidad de Productos')
        ax4.set_title(f'Distribución de Precios - {categoria_sel}')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig4)
    
    # Gráfico 2: Top productos por cantidad
    st.subheader("🏆 Top 10 Productos Más Vendidos")
    
    top_productos = df_filtrado['product_id'].value_counts().head(10)
    
    fig5, ax5 = plt.subplots(figsize=(10, 4))
    top_productos.plot(kind='bar', color='lightgreen', ax=ax5)
    ax5.set_xlabel('ID del Producto')
    ax5.set_ylabel('Cantidad de Ventas')
    ax5.set_title('Top 10 Productos Más Vendidos (por cantidad)')
    ax5.tick_params(axis='x', rotation=45, labelsize=8)
    plt.tight_layout()
    st.pyplot(fig5)
    
    # Gráfico 3: Evolución temporal (si hay datos de tiempo)
    st.subheader("📅 Evolución de Ventas en el Tiempo")
    
    ventas_por_mes = df_filtrado.groupby(df_filtrado['order_purchase_timestamp'].dt.to_period('M'))['price'].sum()
    
    fig6, ax6 = plt.subplots(figsize=(10, 4))
    ventas_por_mes.plot(kind='line', marker='o', color='dodgerblue', ax=ax6)
    ax6.set_xlabel('Mes')
    ax6.set_ylabel('Ingresos Totales (R$)')
    ax6.set_title('Evolución de Ingresos Mensuales')
    ax6.grid(True, alpha=0.3)
    ax6.tick_params(axis='x', labelsize=8)
    plt.tight_layout()
    st.pyplot(fig6)

# Tab 4: Sobre el proyecto
with tab4:
    st.header("ℹ️ Sobre este proyecto")
    
    st.markdown("""
    ### 🎯 Objetivo
    Este proyecto analiza el comportamiento de las ventas de **Olist**, 
    la mayor tienda por departamentos de Brasil. Se exploran patrones de ventas,
    identificando categorías rentables y comportamiento de precios.
    
    ### 🛠️ Herramientas Utilizadas
    - **Python** y **Pandas** para manipulación de datos
    - **Matplotlib** para visualizaciones
    - **Streamlit** para el despliegue interactivo
    
    ### 📊 Dataset
    El análisis utiliza 3 datasets principales de Olist:
    - **olist_orders_dataset.csv**: 99,441 pedidos
    - **olist_order_items_dataset.csv**: 112,650 ítems
    - **olist_products_dataset.csv**: 32,951 productos
    
    ### 📈 Hallazgos Principales
    - **Categoría top**: Beleza_saude (R$ 1.25M en ingresos)
    - **Precio promedio**: R$ 120.65
    - **Mayoría de pedidos**: Entregados exitosamente (~98%)
    - **Productos más vendidos**: Categorías de utilidades y cuidado personal
    
    ### 📁 Repositorio
    Podés ver el notebook original en:
    [DataScience_Proyects - Proyecto 1](https://github.com/Dandlrt09/DataScience_Proyects/tree/main/Proyecto%201)
    
    **Nota**: Este análisis es de carácter educativo y los hallazgos 
    deben considerarse como insights exploratorios.
    """)

# Footer
st.markdown("---")
st.caption("🛒 E-commerce Olist Analysis | Desarrollado con Streamlit y Pandas")
