def v(c):
    match(c):
        # pelaaja
        case "p":
            return (34, 120, 58);
        case "e":
            return (28, 111, 51);
        case "l":
            return (16, 79, 33);
        case "a":
            return (13, 58, 26);
        
        # ruudut
        case "1":
            return (140, 122, 73);
        case "2":
            return (117, 101, 56);
        case "0":
            return (64, 54, 26);
        
        # ei variä
        case ".":
            return None;