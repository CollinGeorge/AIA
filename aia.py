# Define function to display options
def display_options():
    print("\nWelcome to the Artificial Intelligence Agency. Please select an option from the following menu:\n")
    print("1. AUARS")
    print("2. SKEYES")
    print("3. NEXCOM")
    print("4. PSEYEOP")
    print("5. AURELIUS")
    print("6. TWINFLAME")
    print("7. COIN MIRROR")
    print("8. HORNETS NEST")
    print("9. SLEEP WALKER")
    print("10. CRYSTAL BARS")
    print("11. INTREPID DISC")
    print("12. SHADOW MARK 37")
    print("0. Exit")

# Define function to get user input and display option description
def get_option():
    while True:
        option = input("\nEnter the number of the option you would like to learn more about: ")

        if option.isdigit() and int(option) in range(13):
            # Option descriptions
            if option == "1":
                print("\nAUARS is an automated aerospace reconnaissance, surveillance and target acquisition capability that uses Machine Learning and Artificial Intelligence. Details have been redacted to protect classified information, sources, methods, and intellectual property.")
            elif option == "2":
                print("\nSKEYES encompasses multiple technological and operational capabilties for sensitive intelligence operations. Details have been redacted to protect classified information, sources, methods, and intellectual property.")
            elif option == "3":
                print("\nNEXCOM™\n\nNEX = A connection or series of connections linking two or more things.\nCOM = Communication\n\nNEXCOM™ is a centralized communications system that forwards messages and calls (Voice & Video) from all communications platforms and accounts such as Facebook Messenger, Line, WhatsApp, Discord, Teams, Telegram, etc., using an API. The messages and calls are forwarded to the native application on the users mobile device such as FaceTime, Messages, Phone and Mail. The messages can be identified from the originating platform or kept hidden, consequently, the user simply sees a message that appears no different from a text message, email or call and can reply or answer without the need to use each platforms individual application. This eliminates the need for users to install multiple massaging platforms on a device, thereby reducing the attack surface and improving the device security posture. Additionally, end-to-end encryption is maintained thereby giving the user privacy and data integrity.")
            elif option == "4":
                print("\nPSEYEOP is NATO-like dictionary for operations in physical and cyberspace. Details have been redacted to protect classified information, sources, methods, and intellectual property.")
            elif option == "5":
                print("\nAURELIUS is a counterterrorism and counterinsurgency operations and analysis framework. Details have been redacted to protect classified information, sources, methods, and intellectual property.")
            elif option == "6":
                print("\nTWINFLAME is a personal dating assistant and communications capability that uses Artifical Intelligence and Machine Learning in addition to other technological capabilities. Details have been redacted to protect sources, methods, and intellectual property.")
            elif option == "7":
                print("\nCOIN MIRROR is a counterintelligence capability using Artificial Intelligence, Machine Learning and deep fakes. Details have been redacted to protect classified information, sources, methods, and intellectual property.")
            elif option == "8":
                print("\nHORNETS NEST is a highly senstive intelligence operations capability. Details have been redacted to protect classified information, sources, methods, and intellectual property.")
            elif option == "9":
                print("\nSLEEP WALKER is focused on the development and deployment of 0day exploits for sensitive cyber operations. Details have been redacted to protect classified information, sources, methods, and intellectual property.")
            elif option == "10":
                print("\nCRYSTAL BARS™ is an artificial intelligence (AI) and machine learning (ML) capability that enables the prediction of a chosen financial securities direction of movement with a minimum of 80% accuracy. This is accomplished through the analysis of qualitative data using open source intelligence (OSINT) to quantify market sentiment. Additionally, quantitative analysis is performed using historical liquidity data to measure individual candlesticks (bars), accumulation, distribution, consolidation, and time to identify patterns and correlations.\n\nUsing both qualitative and quantitative data analysis, the prediction model (CRYSTAL BARS™) will output within minutes to several hours the direction of a chosen financial security. It should be noted CRYSTAL BARS™ is not intended for and does not work in dark pool or high frequency trading (HFT). CRYSTAL BARS™ is intended for intraday and short term swing trading.")
            elif option == "11":
                print("\nINTREPID DISC is a Signals Intelligence (SIGINT) Operations capability. Details have been redacted to protect classified information, sources, methods, and intellectual property.")
            elif option == "12":
                print("\nSHADOW MARK 37 is the fusion of man and machine using Aritficial Intelligence, Machine Learning and advanced medical technology to give warfighters strategic battlefield advantages. Details have been redacted to protect classified information, sources, methods, and intellectual property.")
            elif option == "0":
                print("\nExiting program. Bye!")
                return
        else:
            print("\nInvalid option selected. Please select a number between 0 and 12.")
            continue

        while True:
            choice = input("\nWould you like to make another selection? (y/n): ")
            if choice.lower() == "y":
                display_options()
                break
            elif choice.lower() == "n":
                print("\nExiting program. Bye!")
                return
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.")
                continue

# Display options and get user input
display_options()
get_option()
