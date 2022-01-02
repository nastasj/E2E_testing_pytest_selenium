from selenium.webdriver.common.by import By


class FeaturePageLocators:

    CITY_CHOOSER_FIELD = (By.CSS_SELECTOR, '[data-marker="location-chooser/value"]')
    CITY_SEARCH_BOX = (By.CSS_SELECTOR, '[data-marker="region-search-bar/search"]')
    SUBWAY_CHOOSER_FIELD = (By.CSS_SELECTOR, '[data-marker="metro-select/withoutValue"]')
    ALPHABET_CHOOSER_TAB = (By.CSS_SELECTOR, '[class ="css-17syd5g"][tabindex="0"]')
    LINE_CHOOSER_TAB = (By.CSS_SELECTOR, '[class ="mav-6guy9c"][tabindex="-1"]')
    STATIONS_ALPHABET_LIST_FIELD = (By.CLASS_NAME, "mav-qkoz4v")
    STATIONS_ALPHABET_LIST = (By.CLASS_NAME, "mav-s9nsgg")
    STATIONS_LINES_LIST_FIELD = (By.CLASS_NAME, "mav-qkoz4v")
    STATIONS_LINES_LIST = (By.CLASS_NAME, "mav-s9nsgg")
    STATION_LINES_LIST_WITH_CHECKBOXES = (By.CSS_SELECTOR, '[class="mav-s9nsgg"][aria-checked="true"] [class="mav-64vbe8"]')
    ALL_LINES = (By.CSS_SELECTOR, '[class="bX_gx css-13meolr"]')
    LINES_CHOSEN = (By.CLASS_NAME, "mav-12br8wd")
    FLOATING_BUTTON = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/apply"]')
    ALL_STATIONS_CHECKBOX = (By.CSS_SELECTOR, '[aria-checked="true"][data-marker="metro-select-dialog/lines/all"]')
    LIST_EXTENDED = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/lines/expanded"]')
    RESET_BUTTON = (By.CLASS_NAME, 'mav-1c4wqey')
    TABS_GROUP = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/tabs"]')
    SUBWAY_SEARCH_BOX = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/search"]')
    CITY_SUGGESTED = (By.CLASS_NAME, "M2qP9")
    MORE_BUTTON = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/chips/more"]') 