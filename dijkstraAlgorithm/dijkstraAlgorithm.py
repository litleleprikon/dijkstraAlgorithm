inf=float('inf')

class graph:
    def __init__(self):
        self.nodes={
                    '1':{'2':7,'3':9, '6':14, 'marker':False, 'weight':inf},
                    '2':{'1':7,'3':10, '4':15, 'marker':False, 'weight':inf},
                    '3':{'1':9,'2':10, '4':11, '6':2, 'marker':False, 'weight':inf},
                    '4':{'2':15,'3':11,'5':6, 'marker':False, 'weight':inf},
                    '5':{'4':6,'6':9, 'marker':False, 'weight':inf},
                    '6':{'1':14,'3':2,'5':9, 'marker':False, 'weight':inf}                                                    
                    }
        self.counter=0

    def dijkstra(self,node, first=False):
        if self.counter==3:
            pass
        self.counter+=1
        if first:    
            self.nodes[node]['weight']=0
        self.nodes[node]['marker']=True
        minNextValue=inf
        minNext=''
        for key in self.nodes[node]:
            if key is not 'weight' and key is not 'marker' and not self.nodes[key]['marker']:
                if self.nodes[node]['weight']+self.nodes[node][key]<self.nodes[key]['weight']:
                    self.nodes[key]['weight']=self.nodes[node]['weight']+self.nodes[node][key]
                if self.nodes[key]['weight']<minNextValue:
                    minNextValue=self.nodes[key]['weight']
                    minNext=key
        if self.counter<len(self.nodes):
            self.dijkstra(minNext)

if __name__=='__main__':
    gr=graph()
    gr.dijkstra('1',True)
    for key in gr.nodes:
        print(key,gr.nodes[key]['weight'])