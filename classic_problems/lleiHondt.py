import heapq

# Dades basades en la província de Barcelona el 23J
# Resolució de la Llei d'Hondt, basada en heaps (max heap)
# Possible millora: Extendre el codi a tot l'estat, llegint un excel amb els vots per partit i província.

partits = ["JUNTS", "ERC", "CUP", "PSOE", "PODEMOS", "PP", "VOX"]
vots = [256231, 326388, 66656, 946055, 402527, 363857, 200138]
escons = 32

def lleidHondt(partits, vots, escons):
    if len(partits) != len(vots):
        print("Partits i vots han de tenir la mateixa longitud")
        return 
    repartiment = [0]*len(partits)
    heap = [(-vots[i],i) for i in range(len(vots))]
    heapq.heapify(heap)
    for j in range(escons):
       guanyador = (heapq.heappop(heap))[1]
       print("Escó per " + partits[guanyador])
       repartiment[guanyador] += 1
       heapq.heappush(heap, (-vots[guanyador] / (repartiment[guanyador]+1), guanyador))
    return repartiment

repartiment = lleidHondt(partits, vots, escons)
print(repartiment)