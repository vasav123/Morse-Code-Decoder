#morsecode decoder
code={".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g",
      "....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m",
      "-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s",
      "-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z"}
while True:
    try:
        x=raw_input("input:")
        print code[x]
    except:
        print "not a thing"

    
