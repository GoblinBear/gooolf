# Monte Carlo Simulation of a Golf Tournament

## Run

```shell
$ python3 golf.py
```

Input:

```
Golfer	                         Mean	      Standard deviation
Sergio Garcia             	 68.99802084636	  2.8022106094
Tiger Woods               	 69.35135041782	  2.7891506279
Kenny Perry               	 69.91471916678	   2.779164583
Gonzalo Fernandez-Castano 	 70.00454323213	 2.80730658184
Rory McIlroy              	 70.03914628487	 2.81525581752
John Cook                 	 70.07314839476	   2.748840518
Jaco Van Zyl              	 70.08926215876	 2.78426082931
Brandt Snedeker           	 70.17987728156	 2.77189131799
Francesco Molinari        	 70.21681358363	 2.74834473201
Matteo Manassero          	 70.22010792006	 2.77346484857
Rocco Mediate             	 70.24975090651	 2.78827651594
Phil Mickelson            	  70.2831986625	 2.77942880401
Justin Rose               	 70.28785317825	 2.75785755538
Jim Furyk                 	 70.29979751876	 2.74303206415
Luke Donald               	 70.31075778923	 2.75356932454
South Africa              	 70.32676162032	   2.752106981
Charl Schwartzel          	 70.39461420897	 2.78476477706
Duffy Waldorf             	 70.40624211864	 2.75608325682
Darren Fichardt           	 70.42869494626	  2.7804524764
Jay Haas                  	 70.44274917206	   2.712519019
```

Output:

```
            Golfer            | Tournament Score |  Win Fraction  | Top 5 Fraction
-------------------------------------------------------------------------------------
        Sergio Garcia                        276            1.00           1.00
         Tiger Woods                         278            0.00           1.00
         Kenny Perry                         280            0.00           0.60
  Gonzalo Fernandez-Castano                  280            0.00           0.60
         Rory McIlroy                        280            0.00           0.60
          John Cook                          280            0.00           0.60
         Jaco Van Zyl                        280            0.00           0.60
       Brandt Snedeker                       281            0.00           0.00
      Francesco Molinari                     281            0.00           0.00
       Matteo Manassero                      281            0.00           0.00
        Rocco Mediate                        281            0.00           0.00
        Phil Mickelson                       281            0.00           0.00
         Justin Rose                         281            0.00           0.00
          Jim Furyk                          281            0.00           0.00
         Luke Donald                         281            0.00           0.00
         South Africa                        281            0.00           0.00
       Charl Schwartzel                      282            0.00           0.00
        Duffy Waldorf                        282            0.00           0.00
       Darren Fichardt                       282            0.00           0.00
           Jay Haas                          282            0.00           0.00
```
