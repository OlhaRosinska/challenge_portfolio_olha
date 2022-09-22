from pages.base_page import BasePage


class Dashboard (BasePage):
    scouts_panel_header_xpath = "//header/div/h6"
    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    polski_button_xpath = "//*[text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    players_count_xpath = "//*[text()='Players count']"
    matches_count_xpath = "//*[text()='Matches count']"
    reports_count_xpath = "//*[text()='Reports count']"
    events_count_xpath = "//*[text()='Events count']"
    logo_scouts_panel_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[1]"
    scouts_panel_body_xpath = "//div[2]/h2"
    player_match_and_report_management_panel_xpath = "//child::div/p"
    dev_team_contact_button_xpath = "//*[text()='Dev team contact']"
    shortcuts_xpath = "//*[text()='Shortcuts']"
    add_player_button_xpath = "//*[text()='Add player']"
    activity_xpath = "//*[text()='Activity']"
    last_created_player_xpath = "//*[text()='Last created player']"
    super_man_button_xpath = "//*[text()='super man']"
