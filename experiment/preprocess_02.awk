#
# @file      preprocess_02.awk
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     regex & tolower for text cleaning
# @date      2021-11-10 04:24:15
# @version   1.0
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 
BEGIN{
    # do_print_debug = 1
    do_print_debug = 0
    # do_limit_row = 1
    do_limit_row = 0
    num_each_debug = 100
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

    print_debug("crlf & tab -> space")
    gsub(/\\n|\\r|\\t|\\f|\\v/," ")
    
    print_debug("rm https? url")
    gsub(/https?:\/\/([[:alnum:]_\-]+\.)+[[:alnum:]_\-]+(\/[[:alnum:]_\-\.\/?%&]*)?/,"")
    
    print_debug("rm pic url")
    gsub(/pic\.([[:alnum:]_\-]+\.)+[[:alnum:]_\-]+(\/[[:alnum:]_\-\./?%&]*)?/,"")
    
    print_debug("rm mail")
    gsub(/[[:alnum:]_]+([\.\-\+][[:alnum:]_]+)*@[[:alnum:]_]+([\.\-][[:alnum:]_]+)*\.[[:alnum:]_]+([\.\-][[:alnum:]_]+)*/,"")
    # gsub(/[[:alnum:]_]+([\.\-\+][[:alnum:]_]+)*\@[[:alnum:]_]+([\.\-][[:alnum:]_]+)*\.[[:alnum:]_]+([\.\-][[:alnum:]_]+)*/,"")
    
    print_debug("\\xa0, \\u2009, and so on -> space")
    gsub(/\\[a-zA-Z]+[0-9]+/," ")
    
    print_debug("rm other than words, spaces, periods")
    gsub(/[^[:alnum:]_ \.]/,"")
    
    # print_debug("rm spaces beside period")
    # gsub(/ \. | \.|\. /,".")

    print_debug("rm spaces before period")
    gsub(/ +\./,".")

    print_debug("multi periods -> single period")
    gsub(/\.{2,}/,".")
    
    print_debug("multi spaces -> single space")
    gsub(/ {2,}/," ")
    
    print_debug("make lower")
    gsub(/.*/,tolower($0))

    # print_debug("rm 3 consecutive abbreviation periods at beginning of line")
    # gsub(/^(.)\.(.)\.(.)\./,"$1$2$3")
    
    # print_debug("rm 2 consecutive abbreviation periods at beginning of line")
    # gsub(/^(.)\.(.)\./,"$1$2")
    
    # print_debug("rm an abbreviation period at beginning of line")
    # gsub(/^(.)\./,"$1")
    
    # print_debug("rm 7 consecutive abbreviation periods")
    # gsub(/ (.)\.(.)\.(.)\.(.)\.(.)\.(.)\.(.)\./,"$1$2$3$4$5$6$7")
    
    # print_debug("rm 6 consecutive abbreviation periods")
    # gsub(/ (.)\.(.)\.(.)\.(.)\.(.)\.(.)\./,"$1$2$3$4$5$6")
    
    # print_debug("rm 5 consecutive abbreviation periods")
    # gsub(/ (.)\.(.)\.(.)\.(.)\.(.)\./,"$1$2$3$4$5")
    
    # print_debug("rm 4 consecutive abbreviation periods")
    # gsub(/ (.)\.(.)\.(.)\.(.)\./,"$1$2$3$4")
    
    # print_debug("rm 3 consecutive abbreviation periods")
    # gsub(/ (.)\.(.)\.(.)\./,"$1$2$3")
    
    # print_debug("rm 2 consecutive abbreviation periods")
    # gsub(/ (.)\.(.)\./,"$1$2")
    
    # print_debug("rm an consecutive abbreviation period")
    # gsub(/ (.)\./,"$1")
        
    print_debug("rm spaces at beginning of line")
    gsub(/^ +/,"")
    
    print_debug("rm periods at beginning of line")
    gsub(/^\.+/,"")

    print $0
}
END{
}