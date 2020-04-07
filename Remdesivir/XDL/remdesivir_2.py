<?xdl version="0.4.0" ?>

<Synthesis>
  <Hardware>
    <Component
      id="buffer_flask"
      type="buffer_flask" />
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
      id="TMSCN" />
    <Reagent
      id="TMSOTf" />
    <Reagent
      id="brine" />
    <Reagent
      id="dichloromethane" />
    <Reagent
      id="solid sodium bicarbonate" />
    <Reagent
      id="triethylamine" />
    <Reagent
      id="trifluoromethanesulfonic acid" />
    <Reagent
      id="(3R,4R,5R)-2-(4-aminopyrrolo[2,1-f][1,2,4]triazin-7-yl)-3,4-bis(benzyloxy)-5- ((benzyloxy)methyl)tetrahydrofuran-2-ol"
  </Reagents>

  <Procedure>
    <HeatChillToTemp
      vessel="reactor"
      temp="-78°C" />
    <Add
      reagent="(3R,4R,5R)-2-(4-aminopyrrolo[2,1-f][1,2,4]triazin-7-yl)-3,4-bis(benzyloxy)-5- ((benzyloxy)methyl)tetrahydrofuran-2-ol"
      vessel="reactor"
      volume="57.9 g"
      stir="True" />
    <Add
      reagent="dichloromethane"
      vessel="reactor"
      volume="100 mL"
      stir="True" />
    <Add
      reagent="trifluoromethanesulfonic acid"
      vessel="reactor"
      volume="18.3 mL"
      stir="True" />
    <Stir
      vessel="reactor"
      time="10 mins" />
    <Add
      reagent="TMSOTf"
      vessel="reactor"
      volume="38.9 mL"
      dispense_speed="10"
      stir="True" />
    <Stir
      vessel="reactor"
      time="30 mins" />
    <Add
      reagent="TMSCN"
      vessel="reactor"
      volume="56.5 mL"
      dispense_speed="10"
      stir="True" />
    <Stir
      vessel="reactor"
      time="2 hrs" />
    <Add
      reagent="triethylamine"
      vessel="reactor"
      volume="50 mL"
      stir="True" />
    <HeatChillToTemp
      vessel="reactor"
      temp="18°C"
      active="False"
      continue_heatchill="False" />
    <Add
      reagent="solid sodium bicarbonate"
      vessel="reactor"
      mass="80 g"
      stir="True" />
    <Stir
      vessel="reactor"
      time="10 mins" />
    <Separate
      purpose="extract"
      from_vessel="reactor"
      separation_vessel="separator"
      to_vessel="buffer_flask"
      product_bottom="False"
      solvent=""
      n_separations="1"
      waste_phase_to_vessel="separator" />
    <Separate
      purpose="extract"
      from_vessel="separator"
      separation_vessel="separator"
      to_vessel="separator"
      product_bottom="True"
      solvent="dichloromethane"
      solvent_volume="25 mL"
      n_separations="1" />
    <Transfer
      from_vessel="buffer_flask"
      to_vessel="separator"
      volume="all" />
    <Separate
      purpose="wash"
      from_vessel="separator"
      separation_vessel="separator"
      to_vessel="rotavap"
      product_bottom="False"
      solvent="brine"
      through="anhydrous sodium sulfate"
      solvent_volume="25 mL"
      n_separations="1" />
    <Evaporate
      rotavap_name="rotavap"
      temp="50°C"
      pressure="699 mbar"
      time="30 mins"
      mode="auto" />
    <RunColumn
      from_vessel="rotavap"
      to_vessel="reactor"
      column="column" />
  </Procedure>

</Synthesis>