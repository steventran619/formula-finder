from stores.stores import Stores
from emailer.emailer import Mail
import datetime

def main():
    try:
        with Stores() as bot:
            print('''   _       .,             
    `\.____|_\    Formula Finder
      \______/       June 2022
       (_)(_)    by Steven Tran''')
            print("=================================")
            print(">>>  Formula Check Initiated  <<<")
            print("=================================")
            currentTime = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Current date/time: {currentTime}")
            results = bot.report_results()      # See stores.py for stores being checked
            # bot.display_results(results)
            htmlResults = bot.get_HTML_table(results)

            # Initialize E-Mailer
            mail = Mail()
            mail.getSender()
            mail.sendMessage(mail.generateMessage(currentTime, htmlResults))
            wait = input('\nEnter any key to exit\n')
            print("Thank you for using my Formula Finder.\nNow exiting...")
            bot.close()
    except Exception as errors:
        if 'in PATH' in str(errors):
            print(
                'You are trying to run the bot from command line \n'
                'Please add to PATH your Selenium Drivers \n'
                'Windows: \n'
                '    set PATH=%PATH%;C:path-to-your-folder \n \n'
                'Linux: \n'
                '    PATH=$PATH:/path/toyour/folder/ \n'
            )
        else:
            raise

if __name__ == "__main__":
    main()