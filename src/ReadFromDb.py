lstt = []

# DATI DI DEBUG #

numero_sped = 13

lstt.append(['445','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','LORY EXPRESS S.N.C.','Via Montepalma, 1','95125 Catania CT','150','Nessuna annotazione','4','40','19','27/10/2022','Pippo Calò'])
lstt.append(['1990','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Manca pacchetto','5','50','9981','27/10/2022','Pippo Calò'])
lstt.append(['27110','DFG Servizi SRL','Via Corace 27','Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Pacchetto trovato','1','100','881','27/10/2022','Pippo Calò'])
lstt.append(['444','DFG Servizi SRL','Via Corace 27','Catanzaro 88100','Coop SPA','Via Barone, 159','Catanzaro 88100','4500','-','10','110','34','27/10/2022','Pippo Calò'])
lstt.append(['8188','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','LORY EXPRESS S.N.C.','Via Montepalma, 1','95125 Catania CT','150','Nessuna annotazione','4','40','19','27/10/2022','Pippo Calò'])
lstt.append(['9109','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Manca pacchetto','5','50','9981','27/10/2022','Pippo Calò'])
lstt.append(['61','DFG Servizi SRL','Via Corace 27','Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Pacchetto trovato','1','100','881','27/10/2022','Pippo Calò'])
lstt.append(['190','DFG Servizi SRL','Via Corace 27','Catanzaro 88100','Coop SPA','Via Barone, 159','Catanzaro 88100','4500','-','10','110','34','27/10/2022','Pippo Calò'])
lstt.append(['62311','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','LORY EXPRESS S.N.C.','Via Montepalma, 1','95125 Catania CT','150','Nessuna annotazione','4','40','19','27/10/2022','Pippo Calò'])
lstt.append(['8191','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Manca pacchetto','5','50','9981','27/10/2022','Pippo Calò'])
lstt.append(['99011','DFG Servizi SRL','Via Corace 27','Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Pacchetto trovato','1','100','881','27/10/2022','Pippo Calò'])
lstt.append(['555','DFG Servizi SRL','Via Corace 27','Catanzaro 88100','Coop SPA','Via Barone, 159','Catanzaro 88100','4500','-','10','110','34','27/10/2022','Pippo Calò'])
lstt.append(['44444','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','LORY EXPRESS S.N.C.','Via Montepalma, 1','95125 Catania CT','150','Nessuna annotazione','4','40','19','27/10/2022','Pippo Calò'])
lstt.append(['11234','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Manca pacchetto','5','50','9981','27/10/2022','Pippo Calò'])
lstt.append(['123434','DFG Servizi SRL','Via Corace 27','Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Pacchetto trovato','1','100','881','27/10/2022','Pippo Calò'])
lstt.append(['0','DFG Servizi SRL','Via Corace 27','Catanzaro 88100','Coop SPA','Via Barone, 159','Catanzaro 88100','4500','-','10','110','34','27/10/2022','Pippo Calò'])
lstt.append(['2112313','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','LORY EXPRESS S.N.C.','Via Montepalma, 1','95125 Catania CT','150','Nessuna annotazione','4','40','19','27/10/2022','Pippo Calò'])
lstt.append(['900','DFG Servizi SRL','Via Corace 27', 'Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Manca pacchetto','5','50','9981','27/10/2022','Pippo Calò'])
lstt.append(['6616','DFG Servizi SRL','Via Corace 27','Catanzaro, 88100','Talmone Gift S.R.L','Via Jannelli, 15','Catanzaro 88100','470','Pacchetto trovato','1','100','881','27/10/2022','Pippo Calò'])
lstt.append(['7789','DFG Servizi SRL','Via Corace 27','Catanzaro 88100','Coop SPA','Via Barone, 159','Catanzaro 88100','4500','-','10','110','34','27/10/2022','Pippo Calò'])

#
# Far ritornare la lista dopo averla presa dal DB
#
def read_from_db():
    return lstt

def numero_spedizioni():
    return numero_sped
    
    
