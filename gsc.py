# -------------
# Streamlit App Configuration
# -------------

def setup_streamlit():
    """
    Configures Streamlit's page settings and displays the app title and markdown information.
    Sets the page layout, title, and markdown content with links and app description.
    """
    st.set_page_config(page_title="✨ Simple Google Search Console Data | LeeFoot.co.uk", layout="wide")
    st.title("✨ Simple Google Search Console Data | Dec 23")
    st.markdown(f"### Lightweight GSC Data Extractor. (Max {MAX_ROWS:,} Rows)")

    st.markdown(
        """
        <p>
            Created by <a href="https://twitter.com/LeeFootSEO" target="_blank">LeeFootSEO</a> |
            <a href="https://leefoot.co.uk" target="_blank">More Apps & Scripts on my Website</a>
        """,
        unsafe_allow_html=True
    )
    st.divider()

def show_display_mode_selector():
    """
    Displays a dropdown selector for choosing the display mode.
    Returns the selected display mode.
    """
    return st.sidebar.selectbox(
        "Select Display Mode:",
        ["Table", "Chart"],
        index=0,
        key='display_mode_selector'
    )

# -------------
# Main Streamlit App Function
# -------------

# Main Streamlit App Function
def main():
    """
    The main function for the Streamlit application.
    Handles the app setup, authentication, UI components, and data fetching logic.
    """
    setup_streamlit()
    display_mode = show_display_mode_selector()
    client_config = load_config()
    st.session_state.auth_flow, st.session_state.auth_url = google_auth(client_config)

    query_params = st.experimental_get_query_params()
    auth_code = query_params.get("code", [None])[0]

    if auth_code and not st.session_state.get('credentials'):
        st.session_state.auth_flow.fetch_token(code=auth_code)
        st.session_state.credentials = st.session_state.auth_flow.credentials

    if not st.session_state.get('credentials'):
        show_google_sign_in(st.session_state.auth_url)
    else:
        init_session_state()
        account = auth_search_console(client_config, st.session_state.credentials)
        properties = list_gsc_properties(st.session_state.credentials)

        if properties:
            webproperty = show_property_selector(properties, account)
            search_type = show_search_type_selector()
            date_range_selection = show_date_range_selector()
            start_date, end_date = calc_date_range(date_range_selection)
            selected_dimensions = show_dimensions_selector(search_type)
            
            if display_mode == "Table":
                show_fetch_data_button(webproperty, search_type, start_date, end_date, selected_dimensions)
            elif display_mode == "Chart":
                report = fetch_data_loading(webproperty, search_type, start_date, end_date, selected_dimensions)
                if report is not None:
                    st.line_chart(report.set_index('date'))  # Show data in a line chart

if __name__ == "__main__":
    main()
