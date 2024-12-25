from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def canvas_login(username, password):
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

    try:
        # Navigate to UC Davis Canvas login page
        driver.get("https://login.canvas.ucdavis.edu/")

        # Wait for the UC Davis Login button to appear
        wait = WebDriverWait(driver, 10)
        ucdavis_login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'marketing-highlight__cta--btn') and text()='UC Davis Log In']")
        ))
        ucdavis_login_button.click()

        # Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.ID, "username")))

        # Locate username and password fields
        username_field = driver.find_element(By.ID, "username")  # Replace with actual ID if different
        password_field = driver.find_element(By.ID, "password")  # Replace with actual ID if different

        # Input credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for Duo authentication to complete
        print("Waiting for Duo Push approval...")
        max_wait_time = 120  # Maximum time to wait for Duo approval (in seconds)
        start_time = time.time()

        while time.time() - start_time < max_wait_time:
            current_url = driver.current_url
            if "dashboard" in current_url:
                print("Login successful! You are now on the dashboard.")
                break
            elif "2fa" not in current_url:
                print("It seems the Duo Push authentication was approved.")
                break
            time.sleep(5)  # Check every 5 seconds
        else:
            print("Duo Push approval timed out. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

        
if __name__ == "__main__":
    # Prompt user for credentials
    #username = input("Enter your UC Davis Canvas username: ")
    #password = input("Enter your UC Davis Canvas password: ")

    username = "khfong"
    password = "Awesomestuff6!"

    # Login to Canvas
    canvas_login(username, password)
