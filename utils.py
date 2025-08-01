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
        case "1": # hiekkaväri 1
            return (140, 122, 73);
        case "2": # hiekkaväri 2
            return (117, 101, 56);
        

        case "v": # reunavuoret vaalea
            return (136, 136, 136);
        case "w": # reunavuoret keski
            return (105, 105, 105);
        case "u": # reunavuoret tumma
            return (88, 88, 88);
        

        # kolikon keltainen
        case "t": # tumma
            return (201, 178, 26);
        case "y": # vaalea
            return (227, 200, 25);

        # lippu
        case "c": # valkoinen
            return (255, 255, 255);
        case "x": # tutun junaliikenteen vihreä
            return (28, 132, 57);

        # ei variä
        case ".":
            return None;