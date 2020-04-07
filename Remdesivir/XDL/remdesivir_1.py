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
      id="10 % aqueous sodium bicarbonate solution" />
    <Reagent
      id="2,3,5-tri-O- benzyl-D-ribono-1,4 lactone tetrahydrofuran solution" />
    <Reagent
      id="7-iodopyrrolo [ 2,1-f ] [ 1,2,4 ] triazin-4-amine" />
    <Reagent
      id="PhMgCl (2 M in tetrahydrofuran)" />
    <Reagent
      id="TMSCl" />
    <Reagent
      id="acetic acid" />
    <Reagent
      id="brine" />
    <Reagent
      id="iPrMgCl (1 M in tetrahydrofuran)" />
    <Reagent
      id="methanol" />
    <Reagent
      id="tetrahydrofuran" />
    <Reagent
      id="water" />
  </Reagents>

  <Procedure>
    <Add
      reagent="7-iodopyrrolo [ 2,1-f ] [ 1,2,4 ] triazin-4-amine"
      vessel="reactor"
      volume="0"
      stir="False" />
    <Add
      reagent="tetrahydrofuran"
      vessel="reactor"
      volume="150 mL"
      stir="False" />
    <Add
      reagent="TMSCl"
      vessel="reactor"
      volume="6.07 mL"
      stir="True" />
    <HeatChill
      vessel="reactor"
      temp="25°C"
      time="10 mins" />
    <HeatChillToTemp
      vessel="reactor"
      temp="0°C" />
    <Add
      reagent="PhMgCl (2 M in tetrahydrofuran)"
      vessel="reactor"
      volume="23.9 mL"
      dispense_speed="10"
      stir="True" />
    <Stir
      vessel="reactor"
      time="20 mins" />
    <Add
      reagent="iPrMgCl (1 M in tetrahydrofuran)"
      vessel="reactor"
      volume="25.1 mL"
      stir="True" />
    <Stir
      vessel="reactor"
      time="15 mins" />
    <HeatChillToTemp
      vessel="reactor"
      temp="-20°C" />
    <Add
      reagent="2,3,5-tri-O- benzyl-D-ribono-1,4 lactone tetrahydrofuran solution"
      vessel="reactor"
      volume="30 mL"
      dispense_speed="10"
      stir="True" />
    <Stir
      vessel="reactor"
      time="60 mins" />
    <HeatChillToTemp
      vessel="reactor"
      temp="0°C"
      active="False" />
    <Add
      reagent="methanol"
      vessel="reactor"
      volume="20 mL"
      stir="True" />
    <Add
      reagent="acetic acid"
      vessel="reactor"
      volume="20 mL"
      stir="True" />
    <Add
      reagent="water"
      vessel="reactor"
      volume="20 mL"
      stir="True" />
    <HeatChillToTemp
      vessel="reactor"
      temp="25°C"
      active="False"
      continue_heatchill="False" />
    <Transfer
      from_vessel="reactor"
      to_vessel="rotavap"
      volume="all" />
    <Evaporate
      rotavap_name="rotavap"
      temp="50°C"
      pressure="169.6667 mbar"
      time="30 mins"
      mode="auto" />
    <Separate
      purpose="wash"
      from_vessel="separator"
      separation_vessel="separator"
      to_vessel="separator"
      product_bottom="False"
      solvent="10 % aqueous sodium bicarbonate solution"
      solvent_volume="250 mL"
      n_separations="1" />
    <Separate
      purpose="wash"
      from_vessel="separator"
      separation_vessel="separator"
      to_vessel="reactor"
      product_bottom="False"
      solvent="brine"
      through="anhydrous sodium sulfate"
      solvent_volume="250 mL"
      n_separations="1" />
    <RunColumn
      from_vessel="reactor"
      to_vessel="reactor"
      column="column" />
  </Procedure>

</Synthesis>