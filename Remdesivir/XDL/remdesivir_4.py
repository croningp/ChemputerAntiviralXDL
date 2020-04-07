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


    <Reagent
      id="ethyl acetate" />
    <Reagent
      id="solid sodium bicarbonate" />
    <Reagent
      id="sulfuric acid" />
    <Reagent
      id="water" />
    <Reagent
      id="2,2-dimethoxypropane" />
    <Reagent
      id="Nuc" />
  </Reagents>

  <Procedure>
    <Add
      reagent="sulfuric acid"
      vessel="reactor"
      volume="1.4 mL"
      stir="True" />
    <Add
      reagent="Nuc"
      vessel="reactor"
      volume="5.8 g"
      stir="True" />
     <Add
      reagent="2,2-dimethoxypropane"
      vessel="reactor"
      volume="12 mL"
      stir="True" />
    <Stir
      vessel="reactor"
      time="30 mins" />
    <HeatChillToTemp
      vessel="reactor"
      temp="45°C" />
    <Stir
      vessel="reactor"
      time="30 mins" />
    <HeatChillToTemp
      vessel="reactor"
      temp="25°C"
      active="False"
      continue_heatchill="False" />
    <Add
      reagent="solid sodium bicarbonate"
      vessel="reactor"
      mass="5.8 g"
      stir="True" />
    <Add
      reagent="water"
      vessel="reactor"
      volume="5.8 mL"
      stir="True" />
    <Stir
      vessel="reactor"
      time="15 mins" />
    <Evaporate
      rotavap_name="rotavap"
      temp="50°C"
      pressure="42 mbar"
      time="30 mins"
      mode="auto" />
    <Add
      reagent="ethyl acetate"
      vessel="rotavap"
      volume="150 mL"
      stir="False" />
    <Dissolve
      vessel="rotavap"
      solvent="water"
      volume="50 mL" />
    <Transfer
      from_vessel="rotavap"
      to_vessel="separator"
      volume="all" />
    <Separate
      purpose="extract"
      from_vessel="separator"
      separation_vessel="separator"
      to_vessel="rotavap"
      product_bottom="False"
      solvent="ethyl acetate"
      through="anhydrous sodium sulfate"
      solvent_volume="50 mL"
      n_separations="2" />
    <Evaporate
      rotavap_name="rotavap"
      temp="50°C"
      pressure="42 mbar"
      time="30 mins"
      mode="auto" />
  </Procedure>

</Synthesis>