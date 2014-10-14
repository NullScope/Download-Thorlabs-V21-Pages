import urllib, sys
import os
import multiprocessing


if not os.path.exists("thorlabs-v21"):
    os.makedirs("thorlabs-v21")


def downloader(page):
    response = urllib.URLopener()
    try:
        response.retrieve('http://www.thorlabs.com/catalogpages/V21/'+str(page)+'.pdf', 'thorlabs-v21/' + str(page).zfill(4) + '.pdf')
    except IOError as error:
        if error[1] == 404:
            print "Page" + str(page).zfill(4) + "not found!\n"

result_queue = multiprocessing.Queue()

def main(argv):
    currentPage = 0
    totalPages = 1904
    max_children = 5

    while currentPage <= totalPages:
        if len(multiprocessing.active_children()) <= max_children:
            currentPage = currentPage + 1
            print "Downloading page "+ str(currentPage).zfill(4) + " out of 1904"
            process = multiprocessing.Process(target=downloader, args=[currentPage])
            process.start()

try:
    if __name__ == '__main__':
        main(sys.argv[1:])
except SystemExit:
    zf.close()
