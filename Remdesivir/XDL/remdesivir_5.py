<?xdl version="0.4.0" ?>

<Synthesis>
  <Hardware>
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
      id="5 % aqueous citric acid solution" />
    <Reagent
      id="5 % aqueous potassium carbonate solution" />
    <Reagent
      id="N,N-diisopropylethylamine" />
    <Reagent
      id="(2S)-2-ethylbutyl 2-(((4- nitrophenoxy)(phenoxy)phosphoryl)amino)propanoate" />
    <Reagent
      id="(3aR,4R,6R,6aR)-4-(4-aminopyrrolo[2,1-f][1,2,4]triazin-7-yl)-6-(hydroxymethyl)-2,2- dimethyltetrahydrofuro[3,4-d][1,3]dioxole-4-carbonitrile" />
    <Reagent
      id="magnesium chloride " />
    <Reagent
      id="brine" />
    <Reagent
      id="ethyl acetate" />
    <Reagent
      id="saturated aqueous ammonium chloride solution" />
  </Reagents>

  <Procedure>
    <HeatChillToTemp
      vessel="reactor"
      temp="25°C" />
    <Add
      reagent="(2S)-2-ethylbutyl 2-(((4- nitrophenoxy)(phenoxy)phosphoryl)amino)propanoate"
      vessel="reactor"
      volume="1.79 g"
      stir="True" />
    <Add
      reagent="(3aR,4R,6R,6aR)-4-(4-aminopyrrolo[2,1-f][1,2,4]triazin-7-yl)-6-(hydroxymethyl)-2,2- dimethyltetrahydrofuro[3,4-d][1,3]dioxole-4-carbonitrile"
      vessel="reactor"
      volume="1.10 g"
      stir="True" />
    <Add
      reagent="magnesium chloride"
      vessel="reactor"
      volume="0.316 g"
      stir="True" />
    <HeatChill
      vessel="reactor"
      temp="50°C"
      time="10 mins" />
    <Add
      reagent="N,N-diisopropylethylamine"
      vessel="reactor"
      volume="1.45 mL"
      stir="True" />
    <Stir
      vessel="reactor"
      time="30 mins" />
    <HeatChillToTemp
      vessel="reactor"
      temp="25°C"
      active="False"
      continue_heatchill="False" />
    <Add
      reagent="ethyl acetate"
      vessel="reactor"
      volume="100 mL"
      stir="True" />
    <Separate
      purpose="wash"
      from_vessel="reactor"
      separation_vessel="separator"
      to_vessel="separator"
      product_bottom="False"
      solvent="5 % aqueous citric acid solution"
      solvent_volume="40 mL"
      n_separations="1" />
    <Separate
      purpose="wash"
      from_vessel="separator"
      separation_vessel="separator"
      to_vessel="separator"
      product_bottom="False"
      solvent="saturated aqueous ammonium chloride solution"
      solvent_volume="40 mL"
      n_separations="1" />
    <Separate
      purpose="wash"
      from_vessel="separator"
      separation_vessel="separator"
      to_vessel="separator"
      product_bottom="False"
      solvent="5 % aqueous potassium carbonate solution"
      solvent_volume="40 mL"
      n_separations="2" />
    <Separate
      purpose="wash"
      from_vessel="separator"
      separation_vessel="separator"
      to_vessel="rotavap"
      product_bottom="False"
      solvent="brine"
      through="anhydrous sodium sulfate"
      solvent_volume="40 mL"
      n_separations="1" />
    <Evaporate
      rotavap_name="rotavap"
      temp="50°C"
      pressure="153 mbar"
      time="30 mins"
      mode="auto" />
    <RunColumn
      from_vessel="rotavap"
      to_vessel="reactor"
      column="column" />
  </Procedure>

</Synthesis>
