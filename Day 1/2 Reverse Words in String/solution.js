/**
 * @param {string} s
 * @return {string}
 */

var reverseWords = function (s) {
    var reversed = ""
    var word = ""
    var spaceFound = false

    for (var i = 0; i < s.length; i++) {
        if (s[i] != " ") {
            word += s[i]
            spaceFound = false
        }
        else {
            reversed = word + reversed
            word = ""

            if (!spaceFound) {
                reversed = " " + reversed
            }
            spaceFound = true
        }
    }
    reversed = word + reversed

    return reversed.trim()
};