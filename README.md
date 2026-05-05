# 🛒 E-commerce Olist Analysis

Una aplicación interactiva de **Análisis de Datos** que explora el comportamiento de ventas de **Olist**, la mayor tienda por departamentos de Brasil.

![Streamlit App](https://img.shields.io/badge/Streamlit-1.45+-FF4B4B?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.2+-150458?logo=pandas)

---

## 🎯 Descripción

Este proyecto analiza el conjunto de datos de **Olist**, integrando información de pedidos, ítems y productos para descubrir patrones de ventas, identificar categorías rentables y analizar el comportamiento de precios.

### ✨ Características

- 📊 **Exploración de Datos**: Vista interactiva del dataset combinado (112K+ ítems)
- 📈 **Análisis**: Top categorías por ingresos, distribución de precios, estatus de pedidos
- 📊 **Visualizaciones Interactivas**: Filtros dinámicos por categoría y estatus, gráficos de evolución temporal
- ℹ️ **Sobre el Proyecto**: Contexto, herramientas utilizadas y enlaces al repositorio original

---

## 🛠️ Tecnologías

- **Python 3.10+**
- **Streamlit** - Interfaz web interactiva
- **Pandas** - Manipulación y análisis de datos
- **Matplotlib** - Visualizaciones

---

## 📊 Datasets Utilizados

El análisis integra 3 datasets principales de Olist:

| Dataset | Registros | Descripción |
|---------|-----------|-------------|
| `olist_orders_dataset.csv` | 99,441 | Información de pedidos |
| `olist_order_items_dataset.csv` | 112,650 | Ítems de cada pedido |
| `olist_products_dataset.csv` | 32,951 | Catálogo de productos |

**Dataset combinado:**
- **112,650 ítems** procesados
- **Precio promedio**: R$ 120.65
- **Categoría top**: Beleza e Saúde

---

## 📈 Hallazgos Principales

| Métrica | Valor |
|---------|-------|
| **Total de pedidos** | 99,441 |
| **Total de ítems** | 112,650 |
| **Precio promedio** | R$ 120.65 |
| **Categoría top** | Beleza e Saúde |
| **Estatus más común** | delivered (~98%) |

### Top 5 Categorías por Ingresos:
1. **Beleza e Saúde** - R$ 1.25M
2. **Relogios Presentes** - R$ 1.20M
3. **Cama Mesa Banho** - R$ 1.03M
4. **Esporte Lazer** - R$ 988K
5. **Informática Acessórios** - R$ 911K

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/Dandlrt09/E-Commerce-app.git
cd E-Commerce-app
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```
*(Si no tenés el archivo, instalá manualmente: `pip install streamlit pandas matplotlib numpy`)*

### 3. Ejecutar la app
```bash
streamlit run app.py
```

La app se abrirá en tu navegador en `http://localhost:8501`.

---

## 📊 Estructura del Proyecto

```
E-Commerce-app/
├── app.py              # Aplicación principal de Streamlit
├── olist_orders.csv   # Dataset de pedidos (17MB)
├── olist_items.csv     # Dataset de ítems (15MB)
├── olist_products.csv   # Dataset de productos (2.3MB)
├── requirements.txt    # Dependencias (solo 3 librerías)
└── README.md          # Este archivo
```

---

## 🔗 Enlaces Relacionados

- **Repositorio original del proyecto**: [DataScience_Proyects - Proyecto 1](https://github.com/Dandlrt09/DataScience_Proyects/tree/main/Proyecto%201)
- **Notebook de análisis**: [Main.ipynb](https://github.com/Dandlrt09/DataScience_Proyects/blob/main/Proyecto%201/Main.ipynb)
- **Portafolio personal**: [danieldlrt09.github.io/Portafolio_Personal](https://danieldlrt09.github.io/Portafolio_Personal/)

---

## 📝 Notas

- El análisis utiliza **3 datasets combinados** para obtener una vista 360° de las ventas
- La app permite **filtros interactivos** por categoría y estatus de pedido
- Este análisis es de carácter educativo y los hallazgos deben considerarse como insights exploratorios
- Los ingresos se expresan en **Reales brasileños (R$)**

---

## 📄 Licencia

Este proyecto es de uso educativo y hace parte del portafolio de Data Science.

**Desarrollado por** [Daniel Del Río](https://github.com/Dandlrt09) 🛒
