from seqbio.calculation.SeqCal import countBase,gcContent,atContent,countBasesDict
from seqbio.pattern.SeqPattern import cpgSearch,enzTargetsScan
from seqbio.seqMan.dnaconvert import *

def argparserLocal():
    from argparse import ArgumentParser
    parser = ArgumentParser(prog='myseq', description='Work with sequence')
    
    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq",  required=True,
                             help="Provide sequence")


    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq",  required=True,
                             help="Provide sequence")
    count_command.add_argument('-r','--revcomp',  action='store_true',
                               help='Convert DNA to reverse-complementary')
    
    transcri_command = subparsers.add_parser('transcription', help= 'Convert DNA->RNA')
    transcri_command.add_argument("-s", "--seq",  required=True,
                             help="Provide sequence")
    transcri_command.add_argument('-r','--revcomp' , action='store_true',
                               help='Convert DNA to reverse-complementary')


    transla_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    transla_command.add_argument("-s", "--seq",  required=True,
                             help="Provide sequence")
    transla_command.add_argument('-r','--revcomp' , action='store_true',
                               help='Convert DNA to reverse-complementary')

    enzTar_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzTar_command.add_argument("-s", "--seq",  required=True,
                             help="Provide sequence")
    enzTar_command.add_argument('-e','--enz', required=True,
                                help='Enzyme name')
    enzTar_command.add_argument('-r','--revcomp' ,action='store_true',
                               help='Convert DNA to reverse-complementary')

    return parser

# Input
def main():
    parser = argparserLocal()
    args = parser.parse_args()

    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()
        # print(seq)
    
    # # Input
    # # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        
        elif args.revcomp:
            rev_seq = reverseComplementSeq(seq)
            print("Input",seq,"\ncountBases =", countBasesDict(rev_seq))
        else:
            print("Input",args.seq,"\ncountBases =", countBasesDict(seq))
        
    
    elif args.command == 'cpgScan':
        if args.seq == None:
            exit(parser.parse_args(['cpgScan','-h']))
        print("Input",args.seq,"\ncpgScan =", cpgSearch(seq))

    elif args.command =='enzTargetsScan':
        if args.seq is None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        if args.revcomp:
            seq = reverseComplementSeq(seq)
            if args.enz == 'EcoRI':
                EcoRI_site = enzTargetsScan(seq,args.enz)
                print('Input',args.seq,'\nEcoRI sites =',EcoRI_site)
            elif args.enz == 'BamHI':
                BamHI_site = enzTargetsScan(seq,args.enz)
                print('Input',args.seq,'\nBamHI sites =',BamHI_site)
            elif args.enz == 'HindIII':
                HindIII_site = enzTargetsScan(seq,args.enz)
                print('Input',args.seq,'\nHindIII sites =',HindIII_site)
            elif args.enz == 'AccB2I':
                AccB2I_site = enzTargetsScan(seq,args.enz)
                print('Input',args.seq,'\nAccB2I sites =',AccB2I_site)
            elif args.enz == 'AasI':
                AasI_site = enzTargetsScan(seq,args.enz)
                print('Input',args.seq,'\nAasI sites =',AasI_site)
            elif args.enz == 'AceI':
                AceI_site = enzTargetsScan(seq,args.enz)
                print('Input',args.seq,'\nAceI sites =',AceI_site) 
            
        elif args.enz == 'EcoRI':
            EcoRI_site = enzTargetsScan(seq,args.enz)
            print('Input',args.seq,'\nEcoRI sites =',EcoRI_site)
        elif args.enz == 'BamHI':
            BamHI_site = enzTargetsScan(seq,args.enz)
            print('Input',args.seq,'\nBamHI sites =',BamHI_site)
        elif args.enz == 'HindIII':
            HindIII_site = enzTargetsScan(seq,args.enz)
            print('Input',args.seq,'\nHindIII sites =',HindIII_site)
        elif args.enz == 'AccB2I':
            AccB2I_site = enzTargetsScan(seq,args.enz)
            print('Input',args.seq,'\nAccB2I sites =',AccB2I_site)
        elif args.enz == 'AasI':
            AasI_site = enzTargetsScan(seq,args.enz)
            print('Input',args.seq,'\nAasI sites =',AasI_site)
        elif args.enz == 'AceI':
            AceI_site = enzTargetsScan(seq,args.enz)
            print('Input',args.seq,'\nAceI sites =',AceI_site) 
        

        

    elif args.command == 'transcription':
        if args.seq is None:
            exit(parser.parse_args(['transcription','-h']))
        elif args.revcomp:
            seq = reverseComplementSeq(seq)
            print("Input",args.seq,"\nTranscription =", dna2rna(seq)) 
        else:
            print("Input",args.seq,"\nTranscription =", dna2rna(seq)) 

    elif args.command == 'translation':
        if args.seq is None:
            exit(parser.parse_args(['translation','-h']))
        elif args.revcomp:
            seq = reverseComplementSeq(seq)
            print("Input",args.seq,"\nTranslation =", dna2protein(seq)) 
        else:
            print("Input",args.seq,"\nTranslation =", dna2protein(seq))
    else:
        parser.print_help()
    

if __name__ == "__main__":
    main()

