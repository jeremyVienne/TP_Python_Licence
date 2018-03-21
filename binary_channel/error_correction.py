import sys
import noisy_transmission
import repeat_three_times
#import hamming

def usage ():
    '''
    `usage ()` indicates how to use the program
    '''
    print( "Usage : %s <method> [<p>] <input> <output>" % sys.argv[0])
    print( "\t<method> = method of error correction (either repeat or hamming)")
    print( "\t<p> = error probability (on one bit). Must be provided only for encoding.")
    print( "\t<input> = filename corresponding to the CBSSM input")
    print( "\t<output> = filename corresponding to the CBSSM output")
    exit(1)

def main ():
    available_method = {
        'repeat': {'encode': repeat_three_times.encode,
                   'decode': repeat_three_times.decode,
                   'decode_nb_bytes': 3,
        },
        'hamming': {'encode': None,
                    'decode': None,
                    'decode_nb_bytes': 2
        }
    }
    
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        usage ()
    else:
        method = sys.argv[1]
        encoding = True
        
        if method not in available_method:
            print ("Method %s is unknown repeat" % method, file=sys.stderr)
            exit(1)

        next_index = 3
        try:
            p = float(sys.argv[2])
        except ValueError:
            encoding = False
            next_index -= 1

        fin = sys.argv[next_index]
        fout = sys.argv[next_index+1]


        if encoding:
            if not available_method[method]['encode']:
                print ("Cannot encode with method %s" % method, file=sys.stderr)
                exit(2)
                
            noisy_transmission.transmit(p, available_method[method]['encode'], fin, fout)
        else:
            info_method = available_method[method]
            if not info_method['decode']:
                print ("Cannot decode with method %s" % method, file=sys.stderr)
                exit(3)
            detected, corrected = noisy_transmission.receive(info_method['decode_nb_bytes'], info_method['decode'], fin, fout)
            print ("%d errors detected (%d corrected)" % (detected, corrected))
            
        exit(0)

if __name__ == '__main__':
    main()
