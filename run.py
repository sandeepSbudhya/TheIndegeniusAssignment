import Scrape as Sc
import sys
import Analyse as An

def main(command):
    if(command == 'analyse'):
        Analyser = An.Analyse()
        Analyser.runAnalyse()
    elif(command == 'scrape'):
        Scraper = Sc.Scrape()
        Scraper.scrapeUrls()
    else:
        print("\n \t Usage:run.py command(command being scrape or analyse) \n")

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        main(sys.argv[1])
        print('\n \t Analysis Complete \n')
    else:
        print("\n \t Usage:run.py command(command being scrape or analyse) \n")