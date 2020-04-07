<?xdl version="0.4.0" ?>

<Synthesis>
  <Hardware>
    <Component
      id="filter"
      type="filter" />
    <Component
      id="reactor"
      type="reactor" />
    <Component
      id="rotavap"
      type="rotavap" />
  </Hardware>

  <Reagents>
    <Reagent
      id="(2R,3R,4R,5R)-2-(4-aminopyrrolo [ 2,1-f ] [ 1,2,4 ] triazin-7-yl)-3,4-bis(benzyloxy)-5-((benzyloxy)methyl)tetrahydrofuran-2-carbonitrile anhydrous dichloromethane solution" />
    <Reagent
      id="boron trichloride" />
    <Reagent
      id="methanol" />
    <Reagent
      id="triethylamine methanol solution" />
    <Reagent
      id="water" />
  </Reagents>

  <Procedure>
    <HeatChillToTemp
      vessel="reactor"
      temp="-78°C" />
    <Add
      reagent="(2R,3R,4R,5R)-2-(4-aminopyrrolo [ 2,1-f ] [ 1,2,4 ] triazin-7-yl)-3,4-bis(benzyloxy)-5-((benzyloxy)methyl)tetrahydrofuran-2-carbonitrile anhydrous dichloromethane solution"
      vessel="reactor"
      volume="5.11 g"
      stir="False" />
    <Add
      reagent="dichloromethane"
      vessel="reactor"
      volume="50 mL"
      stir="False" />
    <Add
      reagent="boron trichloride"
      vessel="reactor"
      volume="35 mL"
      dispense_speed="10"
      stir="True" />
    <HeatChillToTemp
      vessel="reactor"
      temp="-20°C"
      active="False"
      continue_heatchill="False" />
    <Stir
      vessel="reactor"
      time="2 hrs" />
    <HeatChillToTemp
      vessel="reactor"
      temp="-78°C" />
    <Add
      reagent="methanol"
      vessel="reactor"
      volume="10 mL"
      dispense_speed="3"
      stir="True" />
    <Add
      reagent="triethylamine methanol solution"
      vessel="reactor"
      volume="33 mL"
      dispense_speed="3"
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
      pressure="458.5 mbar"
      time="30 mins"
      mode="auto" />
    <Add
      reagent="methanol"
      vessel="reactor"
      volume="50 mL"
      stir="False" />
    <Transfer
      from_vessel="rotavap"
      to_vessel="reactor"
      volume="all" />
    <HeatChillToTemp
      vessel="reactor"
      temp="45°C" />
    <Transfer
      from_vessel="reactor"
      to_vessel="rotavap"
      volume="all" />
    <Add
      reagent="water"
      vessel="rotavap"
      volume="50 mL"
      stir="True" />
    <Evaporate
      rotavap_name="rotavap"
      temp="45°C"
      pressure="319.6667 mbar"
      time="30 mins"
      mode="auto" />
    <Transfer
      from_vessel="rotavap"
      to_vessel="filter"
      volume="all" />
    <HeatChillToTemp
      vessel="filter"
      temp="25°C"
      active="False"
      continue_heatchill="False" />
    <Filter
      filter_vessel="filter" />
    <Dry
      vessel="filter"
      time="16 hrs"
      temp="70°C" />
  </Procedure>

</Synthesis>
