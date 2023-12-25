import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestRegressor
import pickle, joblib
import plotly.express as pe
from streamlit_option_menu import option_menu



# set configuration 
st.set_page_config(
    page_title = 'House Prices In Lagos', 
    page_icon = ':bar_chart:',
    layout = 'wide'
)
# Import Bootsrap CDN 
st.markdown(
        '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">'
        '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js"></script>',
        unsafe_allow_html=True
    )

# Import Tailwind-CSS CDN
st.markdown(
    '<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">',
    unsafe_allow_html=True
)

# Link a CSS file to this notebook 
# with open("styles_streamlit.css") as f:
#        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# import the datasets 
ikeja = pd.read_csv('datasets/production_data/ikeja_deploy.csv')
ikoyi = pd.read_csv('datasets/production_data/ikoyi_deploy.csv')
lekki = pd.read_csv('datasets/production_data/lekki_deploy.csv')
ajah = pd.read_csv('datasets/production_data/ajah_deploy.csv')
agege = pd.read_csv('datasets/production_data/agege_deploy.csv')
vi = pd.read_csv('datasets/production_data/vi_deploy.csv')
yaba = pd.read_csv('datasets/production_data/yaba_deploy.csv')




    # HTML content with classes
html_content = f"""
<div class="test_cont">
    <div class="marquee">
        <div class="cont1">
            <p class="p_sliders">IKEJA</p>
            <p class="p_slider">1million - 3million</p>
        </div>
        <div class="cont1">
            <p class="p_sliders">IKOYI</p>
            <p class="p_slider">1million- 100million</p>
        </div>
        <div class="cont1">
            <p class="p_sliders">LEKKI</p>
            <p class="p_slider">1million - 400million</p>
        </div>
        <div class="cont1">
            <p class="p_sliders">AJAH</p>
            <p class="p_slider">700k - 100million</p>
        </div>
        <div class="cont1">
            <p class="p_sliders">AGEGE</p>
            <p class="p_slider">200k - 3million</p>
        </div>
        <div class="cont1">
            <p class="p_sliders">Victoria Island</p>
            <p class="p_slider">3million - 1billion</p>
        </div>
        <div class="cont1">
            <p class="p_sliders">YABA</p>
            <p class="p_slider">700k - 4million</p>
        </div>
    </div>
</div>
"""
# CSS styles
css = """
<style>
    .test_cont {
        border-radius: 20px;
        height: 7rem;
        # width: 60vw;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        box-shadow: rgba(212, 181, 138, 1) 0px 3px 8px;
        # border: 1px solid #B6C4B6;
    }
        .p_sliders{
        color: #323232;
        font-size = 30px;
        font-weight: bold;
        text-align: center;
        margin-top: 0.7rem
    }
    .p_slider {
        color: #323232;
        font-size: 20px;
        font-weight: bold;
        text-align: center; 
        # width: 5.5rem;
        # margin-top: 1.7rem
        
    }
    .marquee{
        # white-space: nowrap;
        box-sizing: border-box;
        animation: marquee 25s linear infinite;
        width: fit-content;
        height: 3rem;
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }
    .marquee:hover {
        animation-play-state: paused;
    }
    @keyframes marquee {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
        
    }
    .marquee div {
        display: inline-block;
        padding: 0 2rem;
    }
    .cont1, .cont2, .cont3, .cont4, .cont5, .cont6, .cont7{
        margin-left: 70px;
        justify-content: center;
        height: 5.5rem;
        width: 17rem;
        border-radius: 30px;
        # box-shadow: 1px 5px 10px rgba(0,0,0,0.2);
        # box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
        box-shadow: rgb(210, 180, 140) 6px 2px 16px 0px, rgba(255, 255, 255, 0.8) -6px -2px 16px 0px;
        # border: 1px solid #B6C4B6;
    }
    .colorful-divider {
        width: 100%;
        height: 2px;
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
    }
    .plot_container{
        border-radius: 20px;
        height: 15rem;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    }
    .h1{
        font-family: Helvetica, sans-serif;
        font-size: 50px;
        font-weight: 700;
        text-align: center;
        color: #291e0f;
        margin-top: -3.5rem
    }
    .predictor{
        font-family: Helvetica, sans-serif;
        font-size: 20px;
        font-weight: 400;
        text-align: center;
        color: #280003;
        # margin-top: -3.5rem
    }
    .col2{
        height: 30rem;
        align-items: center;
        border-radius: 20px;
        justify-content: center;
        margin-top: 2rem;
        padding: 4rem;
        box-shadow: rgba(192, 147, 84, 1) 6px 2px 16px 0px, rgba(247, 241, 234, 1) -6px -2px 16px 0px;
        transition: transform 0.3s
    }

    .col2:hover {
        transform: scale(1.05);
    }
</style>
"""
# Create Town and Suburb Filter 
joint_data = pd.concat([ikeja, lekki, ikoyi, agege, ajah, vi, yaba], axis = 0)

def Home():
    # Render the HTML content and CSS
    st.markdown(css + html_content, unsafe_allow_html=True)

            
    # Display the divider
    st.sidebar.markdown(css + "<hr class = 'colorful-divider'>", unsafe_allow_html=True)


    # Display the divider
    st.markdown("<br>", unsafe_allow_html= True)
    st.markdown(css + "<hr class = 'colorful-divider'>", unsafe_allow_html=True)

    town_col, suburb_col = st.columns(2, gap = 'large')
    with town_col:
        selected_town = st.multiselect('Select Town', options=joint_data.Location.unique(), default=joint_data.Location.unique()[3])

    with suburb_col:
        if selected_town:
            st.multiselect('Select Suburb', options=joint_data.loc[joint_data['Location'].isin(selected_town)]['Location Area'].unique(), 
                        default=joint_data.loc[joint_data['Location'] == selected_town[0]]['Location Area'][0])

    st.sidebar.subheader('Bedroom Filter')
    one_bed = st.sidebar.checkbox('1 Bedroom', value=True, key = '1bed', help = 'Select Only 1Bedroom Apartments')
    two_bed = st.sidebar.checkbox('2 Bedroom', value=False, key = '2bed', help = 'Select Only 2 Bedroom Apartments')
    three_bed = st.sidebar.checkbox('3 Bedroom', value=False, key = '3bed', help = 'Select Only 3 Bedroom Apartments')
    four_bed = st.sidebar.checkbox('4 Bedroom', value=False, key = '4bed', help = 'Select only 4 Bedroom Apartments')
    five_bed = st.sidebar.checkbox('5 Bedroom' , value=False, key = '5bed', help = 'Select 5 Bedroom and Above Apartments')


    # Create a fucntion to plot Plotly BarChart Of Location and Avg Price 
    def locationByPrice(bedrooms):
        fig1_data = joint_data.loc[(joint_data['Location'].isin(selected_town)) & (joint_data['Bedroom'].isin(bedrooms))][['Price', 'Location Area']]
        grouped_fig1_data = fig1_data.groupby('Location Area')[['Price']].mean()
        fig1 = pe.bar(data_frame = grouped_fig1_data,  x = grouped_fig1_data.index, 
                    y = 'Price', width = 1000, height = 450, title = '<b>Location By Average Price</b>')
        # fig1.update_layout(
        #     plot_bgcolor='rgb(249, 245, 246)' )
        fig1.update_traces(marker_color='#533d1e') 
        st.plotly_chart(fig1, use_container_width= True)

    # Create a condition for plotting based on the number bedrooms selected 
    if selected_town:
        if one_bed:
            locationByPrice([1])

        elif two_bed:
            locationByPrice([2])

        elif three_bed:
            locationByPrice([3])
        
        elif four_bed:
            locationByPrice([4])

        elif five_bed:
            locationByPrice([5,6,7,8,9])



    # Create a function to plot price by price classes
    def priceByBin():
        # Create a price bin to classify the houses into classes 
        joint_data['price_bin'] = pd.cut(joint_data['Price'], bins = [0, 1e6, 5e6, 10e6, 20e6, 50e6, 100e6, 100000e6],
                        labels = ['below 1m', '1m - 5m', '5m - 10m', '10m  - 20m', '20m - 50m', '50m - 100m', '100m above'])
        
        fig1_data = joint_data.loc[(joint_data['Location'].isin(selected_town))][['price_bin', 'Price']]
        grouped = fig1_data.groupby('price_bin')[['Price']].mean()
        fig2 = pe.bar(data_frame = grouped,  x = grouped.index, 
                    y = 'Price', height = 450, title = '<b>Price Classes By Price</b>')
        # fig2.update_layout(
        #     plot_bgcolor='rgb(249, 245, 246)' )
        fig2.update_traces(marker_color='#533d1e')  
        return fig2

    # Create a function to plot price by number of bedrooms
    def priceByBedroom():
        fig1_data = joint_data.loc[(joint_data['Location'].isin(selected_town))][['Price', 'Bedroom']]
        grouped = fig1_data.groupby('Bedroom')[['Price']].mean()
        fig3 = pe.bar(data_frame = grouped,  x = grouped.index, 
                    y = 'Price', height = 450, title = '<b>Price By Number of Bedrooms</b>')
        # fig3.update_layout(
        #     plot_bgcolor='rgb(249, 245, 246)' )
        fig3.update_traces(marker_color='#533d1e') 
        return fig3


    # Display the divider
    st.markdown("<br>", unsafe_allow_html= True)
    st.markdown(css + "<hr class = 'colorful-divider'>", unsafe_allow_html=True)


    priceBin, priceBedrooms = st.columns(2)
    with priceBin:
        priceBin.plotly_chart(priceByBin(), use_container_width= True)

    with priceBedrooms:
        priceBedrooms.plotly_chart(priceByBedroom(), use_container_width= True)

# 2388009916
# zenith

def PricePredict():
    # Render the HTML content and CSS
    st.markdown(css + html_content, unsafe_allow_html=True)
  
    # Display the divider
    st.sidebar.markdown(css + "<hr class = 'colorful-divider'>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html= True)
    st.markdown(css + "<hr class = 'colorful-divider'>", unsafe_allow_html=True)

    # Column for town and suburb 
    town_col, suburb_col = st.columns(2, gap = 'large')
    with town_col:
        selected_town = st.selectbox('Choose Your Preferred Town In Lagos', [i for i in joint_data.Location.unique()])

    with suburb_col:
        if selected_town:
            selected_suburb = st.selectbox(f'Choose Your Preferred Suburb In {selected_town}', 
                                           [i for i in joint_data.loc[joint_data['Location'] == selected_town]['Location Area'].unique()])


    # In the 'end_to_end function, we did the following:
        # Imported the LabelEncoder Transformer and the Model
        # Collected imput variables from the user
        # Preprocessed the Location Area input variable
        # Predicted the price of the given features
    def end_to_end(model_address, encoder_address, data_address):
        encode = joblib.load(encoder_address)
        model = joblib.load(model_address)  
        data = pd.read_csv(data_address)

        # Input Variables Declaration 
        bed = st.number_input("Number Of Bedrooms", data['Bedroom'].min(), data['Bedroom'].max())
        bath = st.number_input("Number Of Bathrooms", data['Bathrooms'].min(), data['Bathrooms'].max())
        toilet = st.number_input("Number Of Toilets", data['Toilet'].min(), data['Toilet'].max())

        # Turn input variables to a dataframe 
        input_vars = pd.DataFrame([{'Bedroom': bed, 'Bathrooms': bath, 'Toilet': toilet, 'Location Area': selected_suburb}])
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(css + f"<p class = 'predictor'>Input Variables", unsafe_allow_html=True)
        st.dataframe(input_vars, use_container_width= True)

        # Using Saved Transformer to Transform the new data 
        input_vars['Location Area'] = encode.transform(input_vars['Location Area']) 
        prediction = model.predict(input_vars)

        if st.button('Push To Predict Price'):
            st.markdown(css + f"<p class = 'predictor'>Predicted price for a {bed}Bedroom Apartment in {selected_town}, \
                        {selected_suburb} is {int(prediction[0])} Naira", unsafe_allow_html=True)

    if selected_town.lower() == 'ikeja':
        end_to_end('models/ikeja_model.pkl', 'models/ikeja_encoder.pkl', 'datasets/production_data/ikeja_deploy.csv')

    elif selected_town.lower() == 'ikoyi':
        end_to_end('models/ikoyi_model.pkl', 'models/ikoyi_encoder.pkl', 'datasets/production_data/ikoyi_deploy.csv')

    elif selected_town.lower() == 'yaba':
        end_to_end('models/yaba_model.pkl', 'models/yaba_encoder.pkl', 'datasets/production_data/yaba_deploy.csv')

    elif selected_town.lower() == 'ajah':
        end_to_end('models/ajah_model.pkl', 'models/ajah_encoder.pkl', 'datasets/production_data/ajah_deploy.csv')
        
    elif selected_town.lower() == 'victoria island (vi)':
        end_to_end('models/vi_model.pkl', 'models/vi_encoder.pkl', 'datasets/production_data/vi_deploy.csv')

    elif selected_town.lower() == 'agege':
        end_to_end('models/agege_model.pkl', 'models/agege_encoder.pkl', 'datasets/production_data/agege_deploy.csv')

    elif selected_town.lower() == 'lekki':
        end_to_end('models/lekki_model.pkl', 'models/lekki_encoder.pkl', 'datasets/production_data/lekki_deploy.csv')


def featurePrediction():
    # Render the HTML content and CSS
    st.markdown(css + html_content, unsafe_allow_html=True)
  
    # Display the divider
    st.sidebar.markdown(css + "<hr class = 'colorful-divider'>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html= True)
    st.markdown(css + "<hr class = 'colorful-divider'>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html= True)

    col1, col2 = st.columns([2,1])
    with col1:
        col1.image('image/pngwing2.com(1).png')
    with col2:
        st.markdown(css + f"<p class = 'col2'><b>🏡 Your Dream Home Awaits!</b><br><br>Tell us your budget, we give the best house features. Whether you're looking for a cozy starter home or a \
                    luxurious estate, our expert team will find the perfect property to fit your budget. From stunning views to modern amenities, \
                    we'll help you find the ideal home for you. Contact us today and let's make your real estate dreams a reality!</p>", \
                        unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html= True)
        # Display the divider
    st.markdown(css + "<hr class = 'colorful-divider'>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html= True)

    input_price, features = st.columns([1,2], gap = 'large')
    with input_price:
        minimum = input_price.number_input('Input Your Minimum Budget', value = 500_000)
        maximum = input_price.number_input('Input Your Maximum Budget', value = 1_000_000)
        get_feature = input_price.button('Press To Get Best Houses')

    with features:
        sel_cols = ['Location', 'Location Area', 'Price', 'Bedroom', 'Bathrooms', 'Toilet']
        display_data = joint_data[sel_cols]
        display_data.reset_index(drop = True, inplace = True)
        if get_feature:
            features.dataframe(display_data.loc[(display_data.Price >= minimum) & (display_data.Price <= maximum)], use_container_width= True)


def sidebar():
    st.sidebar.image('image/pngwing.com (3).png', caption = 'Real Estate Agency')
    with st.sidebar:
            selected = option_menu("Main Menu", ["Summary", 'Price Prediction', 'Feature Prediction', 'Github'], 
            icons=['house', 'tags', 'bag-dash', 'github'], menu_icon="cast", default_index=0)
    if selected == 'Summary':
        # st.markdown("<h1 style = 'color: #1F4172; text-align: center; font-family: helvetica '>STARTUP PROJECT</h1>", unsafe_allow_html = True)
        st.markdown(css + "<h1 class = 'h1'>HOUSE PRICES SUMMARY", unsafe_allow_html=True)
        Home()
    
    elif selected == 'Price Prediction':
        # st.markdown("<h1 style = 'color: #1F4172; text-align: center; font-family: helvetica '>STARTUP PROJECT</h1>", unsafe_allow_html = True)
        st.markdown(css + "<h1 class = 'h1'>HOUSE PRICE PREDICTION PLATFORM", unsafe_allow_html=True)
        PricePredict()

    elif selected == 'Feature Prediction':
        st.markdown(css + "<h1 class = 'h1'>FEATURE PREDICTION", unsafe_allow_html=True)
        featurePrediction()

    elif selected == 'Github':
            st.sidebar.markdown("[GitHub](https://github.com)", unsafe_allow_html=True)
        


sidebar()







hide_st_style = """
<style>
#MainMenu {visibility:hidden;}
footer{visibility:hidden;}
header:{visibility:hidden}
</style>
"""

# beige: #DDD0C8


# [theme]
# primaryColor = '#533d1e'
# backgroundColor = "#f4ece1"
# secondaryBackgroundColor = "#d2b48c"
# textColor = "#291e0f"
# font = "Helvetica Neue"

# Tan and Biege