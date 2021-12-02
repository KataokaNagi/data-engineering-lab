#
# @file      preprocess_04_for-debater-dataset.awk
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     regex & tolower for text cleaning
# @see       preprocess_02.awk
# @date      2021-12-03 04:43:57
# @version   1.0
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 
BEGIN{
    do_print_debug = 1
    # do_print_debug = 0
    do_limit_row = 1
    # do_limit_row = 0
    num_each_debug = 1000
}
function print_debug(regex_title) {
    if (do_print_debug) {
        print $0
        print ""
        print ""
        print regex_title
    }
}
{
    if (do_limit_row && NR > num_each_debug) {
        exit
    }

    if (do_print_debug) {
        print ""
        print "##################################################"
        print "article No.", NR
        print "##################################################"
        print ""
    }

    # for debater dataset
    print_debug("rm like [REF or [REF]")
    gsub(/\[[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]\]?/," ")
    # gsub(/\[[a-zA-Z0-9]{1,3}\]?/," ") # error
    # gsub(/\[REF\]?/," ")

    print_debug("add '.' at the end of sentence")
    $0 = $0 "."

    # A-Z -> a-z.
    # debater dataset version
    print_debug("make lower")
    $0=tolower($0)

    # rm a set of charactors
    print_debug("meta char for space -> space")
    gsub(/\\n|\\r|\\t|\\f|\\v/," ")

    print_debug("\\xa0, \\u2009, and so on -> space")
    gsub(/\\[a-zA-Z]+[0-9]+/," ")


    # rm links
    print_debug("rm https? url")
    gsub(/https?:\/\/([a-z0-9_\-]+\.)+[a-z0-9_\-]+(\/[a-z0-9_\-\.\/?%&]*)?/,"")
    
    print_debug("rm pic url")
    gsub(/pic\.([a-z0-9_\-]+\.)+[a-z0-9_\-]+(\/[a-z0-9_\-\.\/?%&]*)?/,"")
    
    print_debug("rm mail")
    gsub(/[a-z0-9_]+([\.\-\+][a-z0-9_]+)*@[a-z0-9_]+([\.\-][a-z0-9_]+)*\.[a-z0-9_]+([\.\-][a-z0-9_]+)*/,"")    


    # clean whole of the txt
    print_debug("rm other than alphabets, numbers, spaces, punctuations")
    gsub(/[^a-z0-9 \.!?]/,"")


    # rm spaces befor punctuations
    print_debug("rm spaces before periods")
    gsub(/ +\./,".")
    print_debug("rm spaces before exclamation marks")
    gsub(/ +!/,"!")
    print_debug("rm spaces before question marks")
    gsub(/ +\?/,"?")
    # print_debug("rm spaces beside period")
    # gsub(/ \. | \.|\. /,".")

    # rm multi punctuations
    print_debug("multi periods -> single period")
    gsub(/\.+/,".")
    # gsub(/\.{2,}/,".")
    print_debug("multi exclamation marks -> single exclamation mark")
    gsub(/!+/,"!")
    # gsub(/!{2,}/,"!")
    print_debug("multi question marks -> single question mark")
    gsub(/\?+/,"?")
    # gsub(/\?{2,}/,"?")    
    print_debug("multi spaces -> single space")
    gsub(/ +/," ")
    # gsub(/ {2,}/," ")
        
    print_debug("rm spaces at beginning of line")
    gsub(/^ +/,"")
    print_debug("rm periods at beginning of line")
    gsub(/^\.+/,"")
    print_debug("rm exclamation marks at beginning of line")
    gsub(/^!+/,"")
    print_debug("rm question marks at beginning of line")
    gsub(/^\?+/,"")

    print $0
}
END{
}