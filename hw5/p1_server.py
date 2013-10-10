"""
Created on Mon Oct  7 20:55:37 2013

@author: Yigong
"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
#import os
#import inspect
host, port = 'localhost', 5054
server = SimpleXMLRPCServer((host, port), allow_none = True)
class ImageMani:    
    def flipUD(self, img_list):
        import pickle
        nrow = len(img_list)
        ncol = len(img_list[0])
        if isinstance(img_list[0][0], float):
            result = [img_list[nrow-1-i] for i in range(nrow)]
        else:
            nlayer = len(img_list[0][0])
            result = [img_list[nrow-1-i] for i in range(nrow)]
        print '@@'
        pickle.dump('img_list', open('server_original.p','wb'))
        pickle.dump('result', open('server_manipulated.p','wb'))
        return result
        
    def conju(self, img_list):
        import pickle
        nrow = len(img_list)
        ncol = len(img_list[0])
        if isinstance(img_list[0][0], float):
            result = [[255- img_list[i][j]for j in range(ncol)] for i in range(nrow)]
        else:
            nlayer = len(img_list[0][0])
            result = [[[255-img_list[i][j][k]  for k in range(nlayer)] for j in range(ncol)] for i in range(nrow)]
        pickle.dump(img_list, open('server_original.p','wb'))
        pickle.dump(result, open('server_manipulated.p','wb'))
        return result
        
    def exchangeRB(self, img_list):
        import pickle
        nrow = len(img_list)
        ncol = len(img_list[0])
        nlayer = len(img_list[0][0])
        result = [[[img_list[i][j][nlayer-1-k]  for k in range(nlayer)] for j in range(ncol)] for i in range(nrow)]
        pickle.dump(img_list, open('server_original.p','wb'))
        pickle.dump(result, open('server_manipulated.p','wb'))
        return result

server.register_instance(ImageMani())

try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'