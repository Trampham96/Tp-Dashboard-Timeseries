# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# 1.0 Title and Introduction with added styling and emojis
st.title("📊 Business Dashboard 🚀")
st.write(
    """
    Welcome to your interactive **Business Dashboard**!  
    Gain insights into sales trends, customer demographics, and product performance at a glance.  
    Start by uploading your business data below.
    """
)

# 2.0 Data Input
st.header("🔼 Upload Your Business Data 🔼")
uploaded_file = st.file_uploader(
    "Choose a CSV File", type="csv", accept_multiple_files=False, help="Ensure your file is in CSV format."
)

# 3.0 App Body - Data Handling
if uploaded_file:
    # Load and display data
    data = pd.read_csv(uploaded_file)
    st.write("🔍 **Preview of the Uploaded Data:**")
    st.dataframe(data.head(), use_container_width=True)

    # 3.1 Sales Insights Section
    st.header("📈 Sales Insights")
    if 'sales_date' in data.columns and 'sales_amount' in data.columns:
        st.subheader("Sales Trends Over Time")
        fig = px.line(
            data,
            x='sales_date',
            y='sales_amount',
            title='📅 Sales Over Time',
            labels={'sales_date': 'Date', 'sales_amount': 'Sales Amount'},
            color_discrete_sequence=['#FF7F50']
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Ensure 'sales_date' and 'sales_amount' columns exist in your data for sales insights.")

    # 3.2 Customer Segmentation by Region
    st.header("🌍 Customer Segmentation")
    if 'region' in data.columns and 'sales_amount' in data.columns:
        st.subheader("Customer Segmentation by Region")
        fig = px.pie(
            data,
            names='region',
            values='sales_amount',
            title='🗺️ Customer Segmentation by Region',
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ Ensure your data has 'region' and 'sales_amount' columns for customer segmentation.")

    # 3.3 Product Analysis Section
    st.header("📦 Product Analysis")
    if 'product' in data.columns and 'sales_amount' in data.columns:
        st.subheader("Top Products by Sales")
        top_products_df = data.groupby('product').sum('sales_amount').nlargest(10, 'sales_amount').reset_index()
        fig = px.bar(
            top_products_df,
            x='product',
            y='sales_amount',
            title="🏆 Top Products By Sales",
            labels={'product': 'Product', 'sales_amount': 'Sales Amount'},
            color='sales_amount',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Ensure your data has 'product' and 'sales_amount' columns for product analysis.")

    # 3.4 Feedback Form
    st.header("📝 Feedback (Your Opinion Counts!)")
    feedback = st.text_area("Please provide any feedback or suggestions.")
    if st.button("Submit Feedback"):
        st.success('✨ Thank you for your feedback! ✨')
        st.balloons()

# 4.0 Footer with additional styling
st.markdown("---")
st.write(
    """
    **This business dashboard template is flexible.**  
    🌟 Customize it further to meet your business needs!
"""
)
