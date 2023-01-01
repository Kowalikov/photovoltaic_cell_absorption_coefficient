## Repozytorium pracy inżynierskiej: "*Obliczenia współczynnika absorpcji dla części aktywnej wielozłączowego ogniwa słonecznego na podłożu GaSb*".



**Głównym celem** tego repozytorium jest dostarczenie kodu wyznaczającego wpółczynnik absorbcji i innych parametrów złącza na zdefiniowanym przez użytkownika podłożu. Repozytorium to ma dostarczyć kod w odtwarzalnej i czytelnej dla innych formie.


Praca inżynierska, kroki:


* Wyznaczenie materiałów do użycia na podłożu GaSb
* Wyznaczyć położenie wierzchołków pasm GaSb
* Wyrysować położenia wierzchołków pasm materiałów na podłożu GaSb
* ...


## Structure:

```
materials/              # materials paramets
src/
    simulations/        # simulations source code for different materials
        IIIA_VA.py      # methods for III-V semiconductors compounds

```



## Environment:

```
conda create --name <conda_env>
conda activate --name <conda_env>
conda install jupyter
pip install ipykernel
pip install mendeleev
pip install matplotlib
pip install seaborn
```


## References:

All of parameters in `materials` folder are linked in files  `' #<reference_link>'` at the end of each line.


To add:
`src/simulators/IIIA_VA/band_gap_from_mole_fraction/` for 'IIIA_2_VA_1` and 'VCA' method


Dobór materiałów:

Ogniwo trójzłączowe ze złączami zbudowanymi z materiałów o przerwach energetycznych 1.8, 1.3 oraz 0.7 [eV].