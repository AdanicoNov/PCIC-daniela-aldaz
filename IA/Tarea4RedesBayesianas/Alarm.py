from redes_bayesianas import BayesianNetwork


edges = [
    ('burglary', 'alarm'),
    ('earthquake', 'alarm'),
    ('alarm', 'jonh_calls'),
    ('alarm', 'mary_calls')
]

bn = BayesianNetwork(edges)
evidence = {'alarm'}

#Primera consulta (B,J|A) Es independiente?
print(bn.d_separation('burglary', 'jonh_calls', evidence, edges)) 

#Segunda consulta (B,E|A) Es independiente?
print(bn.d_separation('burglary', 'earthquake', evidence, edges))  

#Tercera consulta (B,E|A,E) Es independiente
evidence = {'alarm', 'earthquake'}
print(bn.d_separation('burglary', 'earthquake', evidence, edges)) 
