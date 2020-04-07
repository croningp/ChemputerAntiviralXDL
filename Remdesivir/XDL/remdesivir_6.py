<?xdl version="0.4.0" ?>

<Synthesis>
  <Hardware>
    <Component
      id="cartridge_anhydrous sodium sulfate"
      type="cartridge"
      chemical="anhydrous sodium sulfate" />
    <Component
      id="reactor"
      type="reactor" />
    <Component
      id="rotavap"
      type="rotavap" />
    <Component
      id="separator"
      type="separator" />
  </Hardware>

  <Reagents>
    <Reagent
      id="brine" />
    <Reagent
      id="(S)-2-ethylbutyl 2-(((S)-(((3aR,4R,6R,6aR)-6-(4-aminopyrrolo[2,1- f][1,2,4]triazin-7-yl)-6-cyano-2,2-dimethyltetrahydrofuro[3,4-d][1,3]dioxol-4- yl)methoxy)(phenoxy)phosphoryl)amino)propanoate" />
    <Reagent
      id="ethyl acetate" />
    <Reagent
      id="tetrahydrofuran "/>
    <Reagent
      id="propanoate tetrahydrofuran solution" />
    <Reagent
      id="water" />
    <Reagent
      id="saturated aqueous sodium bicarbonate solution" />
  </Reagents>

  <Procedure>
    <HeatChillToTemp
      vessel="reactor"
      temp="0°C" />
    <Add
      reagent="propanoate tetrahydrofuran solution"
      vessel="reactor"
      volume="100 mL"
      stir="True" />
    <Add
      reagent="(S)-2-ethylbutyl 2-(((S)-(((3aR,4R,6R,6aR)-6-(4-aminopyrrolo[2,1- f][1,2,4]triazin-7-yl)-6-cyano-2,2-dimethyltetrahydrofuro[3,4-d][1,3]dioxol-4- yl)methoxy)(phenoxy)phosphoryl)amino)propanoate"
      vessel="reactor"
      volume="12.9 g"
      stir="True" />
    <HeatChillToTemp
      vessel="reactor"
      temp="18°C"
      active="False"
      continue_heatchill="False" />
    <Stir
      vessel="reactor"
      time="5 hrs" />
    <Add
      reagent="water"
      vessel="reactor"
      volume="100 mL"
      stir="True" />
    <Add
      reagent="saturated aqueous sodium bicarbonate solution"
      vessel="reactor"
      volume="200 mL"
      stir="True" />
    <Separate
      purpose="extract"
      from_vessel="reactor"
      separation_vessel="separator"
      to_vessel="separator"
      product_bottom="False"
      solvent="ethyl acetate"
      solvent_volume="100 mL"
      n_separations="1" />
    <Separate
      purpose="wash"
      from_vessel="separator"
      separation_vessel="separator"
      to_vessel="rotavap"
      product_bottom="False"
      solvent="brine"
      through="anhydrous sodium sulfate"
      solvent_volume="50 mL"
      n_separations="1" />
    <Evaporate
      rotavap_name="rotavap"
      temp="50°C"
      pressure="145.5 mbar"
      time="30 mins"
      mode="auto" />
    <RunColumn
      from_vessel="rotavap"
      to_vessel="reactor"
      column="column" />
  </Procedure>

</Synthesis>
