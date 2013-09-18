import urllib2
import re
import pdb
def calculate(input_str, return_float = False):
    try:
        result = eval(input_str,{'__builtins__':{},})
    except:
        input_str = input_str.replace(' ','%20')
        WolframA = urllib2.urlopen('http://api.wolframalpha.com/v2/query?input='+input_str+'&appid=UAGAWR-3X6Y8W777Q')
        content = WolframA.read()        
        subWolframA = re.search(r'title=\'Result\'.*?</plaintext>',content,re.S).group()
        answer = re.search(r'<plaintext>.*</plaintext>',subWolframA,re.S).group()
        result = answer[11:-12]
        result = result.replace('\xc3\x9710^','e')
    if return_float:
        result = float(result)
    else:
        pass
    return result

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='This is a calculator')
    parser.add_argument('question', type = str, help = 'question you wanna ask the calculator')
    parser.add_argument('-v','--version', action = 'store_true', help = 'The version of the calculator' )
    args = parser.parse_args()
    result = calculate(args.question)
    print str(result)
    if args.version:
        print 'This calculator is in version ' + '1.0'
    else:
        pass








        
    
    