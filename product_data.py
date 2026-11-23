"""Approved HM UNIQUE product data (315 products: 5 categories x 7 sub-categories x 9).

Single source for the five category pages. build_pages.py renders the first sub-category's
cards into each page and regenerates the `const CATALOG` block of each js/pages/*-catalog.js
from this data, so initial HTML and JavaScript-rendered states cannot drift.
Product ids are stable lowercase_underscore identifiers reserved for later image mapping.
Descriptions are generic; no brands, ratings, dimensions, certifications or stock claims.
"""

PRODUCT_DATA = {
 "electricals": [
  {
   "key": "wires-cables",
   "label": "Wires & Cables",
   "icon": "fa-plug",
   "intro": "Power, control and signal cables and wires for building and industrial wiring.",
   "products": [
    {
     "id": "frls_copper_building_wire",
     "name": "FRLS Copper Building Wire",
     "description": "Copper wire with FRLS insulation for building wiring.",
     "specs": [
      [
       "Product Type",
       "Building wire"
      ],
      [
       "General Use",
       "Building wiring"
      ],
      [
       "Conductor",
       "Copper"
      ]
     ]
    },
    {
     "id": "single_core_flexible_panel_wire",
     "name": "Single-Core Flexible Panel Wire",
     "description": "Single-core flexible wire for connections inside panels.",
     "specs": [
      [
       "Product Type",
       "Panel wire"
      ],
      [
       "General Use",
       "Panel wiring"
      ],
      [
       "Construction",
       "Single-core, flexible"
      ]
     ]
    },
    {
     "id": "multicore_flexible_copper_cable",
     "name": "Multicore Flexible Copper Cable",
     "description": "Flexible multicore cable with copper conductors for equipment connections.",
     "specs": [
      [
       "Product Type",
       "Flexible cable"
      ],
      [
       "General Use",
       "Equipment connections"
      ],
      [
       "Conductor",
       "Copper"
      ]
     ]
    },
    {
     "id": "armoured_xlpe_power_cable",
     "name": "Armoured XLPE Power Cable",
     "description": "Armoured power cable with XLPE insulation.",
     "specs": [
      [
       "Product Type",
       "Power cable"
      ],
      [
       "General Use",
       "Power distribution"
      ],
      [
       "Construction",
       "Armoured, XLPE"
      ]
     ]
    },
    {
     "id": "unarmoured_xlpe_power_cable",
     "name": "Unarmoured XLPE Power Cable",
     "description": "Unarmoured power cable with XLPE insulation.",
     "specs": [
      [
       "Product Type",
       "Power cable"
      ],
      [
       "General Use",
       "Power distribution"
      ],
      [
       "Construction",
       "Unarmoured, XLPE"
      ]
     ]
    },
    {
     "id": "multicore_control_cable",
     "name": "Multicore Control Cable",
     "description": "Multicore cable for control circuits.",
     "specs": [
      [
       "Product Type",
       "Control cable"
      ],
      [
       "General Use",
       "Control wiring"
      ],
      [
       "Construction",
       "Multicore"
      ]
     ]
    },
    {
     "id": "shielded_instrumentation_cable",
     "name": "Shielded Instrumentation Cable",
     "description": "Shielded cable for instrumentation signals.",
     "specs": [
      [
       "Product Type",
       "Instrumentation cable"
      ],
      [
       "General Use",
       "Signal wiring"
      ],
      [
       "Construction",
       "Shielded"
      ]
     ]
    },
    {
     "id": "welding_cable",
     "name": "Welding Cable",
     "description": "Cable for connecting welding equipment.",
     "specs": [
      [
       "Product Type",
       "Welding cable"
      ],
      [
       "General Use",
       "Welding connections"
      ]
     ]
    },
    {
     "id": "solar_dc_cable",
     "name": "Solar DC Cable",
     "description": "DC cable for solar installations.",
     "specs": [
      [
       "Product Type",
       "Solar cable"
      ],
      [
       "General Use",
       "Solar DC wiring"
      ]
     ]
    }
   ]
  },
  {
   "key": "circuit-protection-switchgear",
   "label": "Circuit Protection & Switchgear",
   "icon": "fa-bolt",
   "intro": "Breakers, residual current devices and isolators for protecting and switching electrical circuits.",
   "products": [
    {
     "id": "single_pole_mcb",
     "name": "Single-Pole MCB",
     "description": "Miniature circuit breaker for circuit protection.",
     "specs": [
      [
       "Product Type",
       "Miniature circuit breaker"
      ],
      [
       "General Use",
       "Circuit protection"
      ],
      [
       "Poles",
       "Single"
      ]
     ]
    },
    {
     "id": "double_pole_mcb",
     "name": "Double-Pole MCB",
     "description": "Miniature circuit breaker for circuit protection.",
     "specs": [
      [
       "Product Type",
       "Miniature circuit breaker"
      ],
      [
       "General Use",
       "Circuit protection"
      ],
      [
       "Poles",
       "Double"
      ]
     ]
    },
    {
     "id": "triple_pole_mcb",
     "name": "Triple-Pole MCB",
     "description": "Miniature circuit breaker for circuit protection.",
     "specs": [
      [
       "Product Type",
       "Miniature circuit breaker"
      ],
      [
       "General Use",
       "Circuit protection"
      ],
      [
       "Poles",
       "Triple"
      ]
     ]
    },
    {
     "id": "four_pole_mcb",
     "name": "Four-Pole MCB",
     "description": "Miniature circuit breaker for circuit protection.",
     "specs": [
      [
       "Product Type",
       "Miniature circuit breaker"
      ],
      [
       "General Use",
       "Circuit protection"
      ],
      [
       "Poles",
       "Four"
      ]
     ]
    },
    {
     "id": "residual_current_circuit_breaker_rccb",
     "name": "Residual Current Circuit Breaker — RCCB",
     "description": "Residual current device for earth-leakage protection.",
     "specs": [
      [
       "Product Type",
       "Residual current device"
      ],
      [
       "General Use",
       "Earth-leakage protection"
      ]
     ]
    },
    {
     "id": "residual_current_breaker_with_overcurrent_protection_rcbo",
     "name": "Residual Current Breaker with Overcurrent Protection — RCBO",
     "description": "Residual current breaker combined with overcurrent protection.",
     "specs": [
      [
       "Product Type",
       "Residual current breaker"
      ],
      [
       "General Use",
       "Circuit protection"
      ]
     ]
    },
    {
     "id": "moulded_case_circuit_breaker_mccb",
     "name": "Moulded Case Circuit Breaker — MCCB",
     "description": "Moulded case circuit breaker for circuit protection and switching.",
     "specs": [
      [
       "Product Type",
       "Circuit breaker"
      ],
      [
       "General Use",
       "Circuit protection"
      ]
     ]
    },
    {
     "id": "switch_disconnector",
     "name": "Switch Disconnector",
     "description": "Switch for isolating a circuit from its supply.",
     "specs": [
      [
       "Product Type",
       "Isolating switch"
      ],
      [
       "General Use",
       "Circuit isolation"
      ]
     ]
    },
    {
     "id": "surge_protection_device_spd",
     "name": "Surge Protection Device — SPD",
     "description": "Device for protecting installations from voltage surges.",
     "specs": [
      [
       "Product Type",
       "Surge protector"
      ],
      [
       "General Use",
       "Surge protection"
      ]
     ]
    }
   ]
  },
  {
   "key": "contactors-relays-motor-starters",
   "label": "Contactors, Relays & Motor Starters",
   "icon": "fa-gears",
   "intro": "Contactors, relays and motor starters for switching and controlling electrical loads.",
   "products": [
    {
     "id": "three_pole_power_contactor",
     "name": "Three-Pole Power Contactor",
     "description": "Contactor for switching power circuits.",
     "specs": [
      [
       "Product Type",
       "Contactor"
      ],
      [
       "General Use",
       "Power switching"
      ],
      [
       "Poles",
       "Three"
      ]
     ]
    },
    {
     "id": "auxiliary_contactor",
     "name": "Auxiliary Contactor",
     "description": "Contactor for control and auxiliary circuits.",
     "specs": [
      [
       "Product Type",
       "Contactor"
      ],
      [
       "General Use",
       "Control circuits"
      ]
     ]
    },
    {
     "id": "thermal_overload_relay",
     "name": "Thermal Overload Relay",
     "description": "Relay for overload protection.",
     "specs": [
      [
       "Product Type",
       "Overload relay"
      ],
      [
       "General Use",
       "Overload protection"
      ]
     ]
    },
    {
     "id": "electronic_motor_protection_relay",
     "name": "Electronic Motor Protection Relay",
     "description": "Electronic relay for motor protection.",
     "specs": [
      [
       "Product Type",
       "Protection relay"
      ],
      [
       "General Use",
       "Motor protection"
      ],
      [
       "Type",
       "Electronic"
      ]
     ]
    },
    {
     "id": "phase_failure_sequence_relay",
     "name": "Phase Failure & Sequence Relay",
     "description": "Relay for monitoring phase failure and phase sequence.",
     "specs": [
      [
       "Product Type",
       "Monitoring relay"
      ],
      [
       "General Use",
       "Supply monitoring"
      ]
     ]
    },
    {
     "id": "timer_relay",
     "name": "Timer Relay",
     "description": "Relay with a time-delay function.",
     "specs": [
      [
       "Product Type",
       "Timer relay"
      ],
      [
       "General Use",
       "Timed switching"
      ]
     ]
    },
    {
     "id": "direct_on_line_motor_starter",
     "name": "Direct-On-Line Motor Starter",
     "description": "Motor starter using the direct-on-line method.",
     "specs": [
      [
       "Product Type",
       "Motor starter"
      ],
      [
       "General Use",
       "Motor starting"
      ],
      [
       "Method",
       "Direct-on-line"
      ]
     ]
    },
    {
     "id": "star_delta_motor_starter",
     "name": "Star-Delta Motor Starter",
     "description": "Motor starter using the star-delta method.",
     "specs": [
      [
       "Product Type",
       "Motor starter"
      ],
      [
       "General Use",
       "Motor starting"
      ],
      [
       "Method",
       "Star-delta"
      ]
     ]
    },
    {
     "id": "motor_protection_circuit_breaker_mpcb",
     "name": "Motor Protection Circuit Breaker — MPCB",
     "description": "Circuit breaker for motor protection.",
     "specs": [
      [
       "Product Type",
       "Circuit breaker"
      ],
      [
       "General Use",
       "Motor protection"
      ]
     ]
    }
   ]
  },
  {
   "key": "switches-sockets-industrial-plugs",
   "label": "Switches, Sockets & Industrial Plugs",
   "icon": "fa-toggle-on",
   "intro": "Switches, sockets and industrial plugs for commercial, industrial and residential installations.",
   "products": [
    {
     "id": "modular_one_way_switch",
     "name": "Modular One-Way Switch",
     "description": "Modular switch for one-way control of a circuit.",
     "specs": [
      [
       "Product Type",
       "Switch"
      ],
      [
       "General Use",
       "On/off control"
      ],
      [
       "Way",
       "One-way"
      ]
     ]
    },
    {
     "id": "modular_two_way_switch",
     "name": "Modular Two-Way Switch",
     "description": "Modular switch for two-way control of a circuit.",
     "specs": [
      [
       "Product Type",
       "Switch"
      ],
      [
       "General Use",
       "Two-point control"
      ],
      [
       "Way",
       "Two-way"
      ]
     ]
    },
    {
     "id": "double_pole_switch_with_indicator",
     "name": "Double-Pole Switch with Indicator",
     "description": "Double-pole switch fitted with an indicator.",
     "specs": [
      [
       "Product Type",
       "Switch"
      ],
      [
       "General Use",
       "On/off control"
      ],
      [
       "Poles",
       "Double, with indicator"
      ]
     ]
    },
    {
     "id": "modular_three_pin_socket",
     "name": "Modular Three-Pin Socket",
     "description": "Modular socket for three-pin plugs.",
     "specs": [
      [
       "Product Type",
       "Socket outlet"
      ],
      [
       "General Use",
       "Plug connection"
      ],
      [
       "Pins",
       "Three"
      ]
     ]
    },
    {
     "id": "industrial_panel_mounted_socket",
     "name": "Industrial Panel-Mounted Socket",
     "description": "Industrial socket outlet for panel mounting.",
     "specs": [
      [
       "Product Type",
       "Industrial socket"
      ],
      [
       "General Use",
       "Equipment connection"
      ],
      [
       "Mounting",
       "Panel"
      ]
     ]
    },
    {
     "id": "industrial_wall_mounted_socket",
     "name": "Industrial Wall-Mounted Socket",
     "description": "Industrial socket outlet for wall mounting.",
     "specs": [
      [
       "Product Type",
       "Industrial socket"
      ],
      [
       "General Use",
       "Equipment connection"
      ],
      [
       "Mounting",
       "Wall"
      ]
     ]
    },
    {
     "id": "industrial_cable_plug",
     "name": "Industrial Cable Plug",
     "description": "Industrial plug fitted to a cable.",
     "specs": [
      [
       "Product Type",
       "Industrial plug"
      ],
      [
       "General Use",
       "Equipment connection"
      ]
     ]
    },
    {
     "id": "industrial_cable_coupler",
     "name": "Industrial Cable Coupler",
     "description": "Industrial coupler for cable connections.",
     "specs": [
      [
       "Product Type",
       "Industrial coupler"
      ],
      [
       "General Use",
       "Cable connection"
      ]
     ]
    },
    {
     "id": "rotary_cam_changeover_switch",
     "name": "Rotary Cam Changeover Switch",
     "description": "Rotary cam switch for changing over between circuits.",
     "specs": [
      [
       "Product Type",
       "Changeover switch"
      ],
      [
       "General Use",
       "Circuit changeover"
      ],
      [
       "Operation",
       "Rotary cam"
      ]
     ]
    }
   ]
  },
  {
   "key": "distribution-boards-panel-accessories",
   "label": "Distribution Boards & Panel Accessories",
   "icon": "fa-table-cells",
   "intro": "Distribution boards and panel accessories for organising and distributing electrical supply.",
   "products": [
    {
     "id": "spn_distribution_board",
     "name": "SPN Distribution Board",
     "description": "Distribution board in SPN configuration.",
     "specs": [
      [
       "Product Type",
       "Distribution board"
      ],
      [
       "General Use",
       "Circuit distribution"
      ],
      [
       "Configuration",
       "SPN"
      ]
     ]
    },
    {
     "id": "tpn_distribution_board",
     "name": "TPN Distribution Board",
     "description": "Distribution board in TPN configuration.",
     "specs": [
      [
       "Product Type",
       "Distribution board"
      ],
      [
       "General Use",
       "Circuit distribution"
      ],
      [
       "Configuration",
       "TPN"
      ]
     ]
    },
    {
     "id": "metal_control_panel_enclosure",
     "name": "Metal Control Panel Enclosure",
     "description": "Metal enclosure for housing control panel equipment.",
     "specs": [
      [
       "Product Type",
       "Panel enclosure"
      ],
      [
       "General Use",
       "Equipment housing"
      ],
      [
       "Material",
       "Metal"
      ]
     ]
    },
    {
     "id": "din_rail",
     "name": "DIN Rail",
     "description": "Rail for mounting DIN-rail components.",
     "specs": [
      [
       "Product Type",
       "Mounting rail"
      ],
      [
       "General Use",
       "Component mounting"
      ]
     ]
    },
    {
     "id": "copper_busbar",
     "name": "Copper Busbar",
     "description": "Copper busbar for conducting and distributing current.",
     "specs": [
      [
       "Product Type",
       "Busbar"
      ],
      [
       "General Use",
       "Current distribution"
      ],
      [
       "Material",
       "Copper"
      ]
     ]
    },
    {
     "id": "neutral_link_earth_bar",
     "name": "Neutral Link & Earth Bar",
     "description": "Bars for neutral and earth connections.",
     "specs": [
      [
       "Product Type",
       "Terminal bar"
      ],
      [
       "General Use",
       "Neutral and earth connections"
      ]
     ]
    },
    {
     "id": "slotted_panel_wiring_duct",
     "name": "Slotted Panel Wiring Duct",
     "description": "Slotted duct for organising panel wiring.",
     "specs": [
      [
       "Product Type",
       "Wiring duct"
      ],
      [
       "General Use",
       "Panel wiring management"
      ],
      [
       "Design",
       "Slotted"
      ]
     ]
    },
    {
     "id": "panel_cooling_fan_filter",
     "name": "Panel Cooling Fan & Filter",
     "description": "Fan and filter for panel ventilation.",
     "specs": [
      [
       "Product Type",
       "Ventilation accessory"
      ],
      [
       "General Use",
       "Panel ventilation"
      ]
     ]
    },
    {
     "id": "panel_indicator_light",
     "name": "Panel Indicator Light",
     "description": "Indicator light for panel mounting.",
     "specs": [
      [
       "Product Type",
       "Indicator light"
      ],
      [
       "General Use",
       "Status indication"
      ],
      [
       "Mounting",
       "Panel"
      ]
     ]
    }
   ]
  },
  {
   "key": "industrial-commercial-lighting",
   "label": "Industrial & Commercial Lighting",
   "icon": "fa-lightbulb",
   "intro": "Lighting for factories, warehouses, offices and other commercial and industrial spaces.",
   "products": [
    {
     "id": "led_high_bay_light",
     "name": "LED High Bay Light",
     "description": "LED light for high-bay lighting.",
     "specs": [
      [
       "Product Type",
       "LED luminaire"
      ],
      [
       "General Use",
       "High-bay lighting"
      ],
      [
       "Light source",
       "LED"
      ]
     ]
    },
    {
     "id": "led_floodlight",
     "name": "LED Floodlight",
     "description": "LED floodlight for area lighting.",
     "specs": [
      [
       "Product Type",
       "LED luminaire"
      ],
      [
       "General Use",
       "Area lighting"
      ],
      [
       "Light source",
       "LED"
      ]
     ]
    },
    {
     "id": "led_streetlight",
     "name": "LED Streetlight",
     "description": "LED light for street lighting.",
     "specs": [
      [
       "Product Type",
       "LED luminaire"
      ],
      [
       "General Use",
       "Street lighting"
      ],
      [
       "Light source",
       "LED"
      ]
     ]
    },
    {
     "id": "led_panel_light",
     "name": "LED Panel Light",
     "description": "LED panel light for indoor lighting.",
     "specs": [
      [
       "Product Type",
       "LED luminaire"
      ],
      [
       "General Use",
       "Indoor lighting"
      ],
      [
       "Light source",
       "LED"
      ]
     ]
    },
    {
     "id": "led_downlight",
     "name": "LED Downlight",
     "description": "LED downlight for general lighting.",
     "specs": [
      [
       "Product Type",
       "LED luminaire"
      ],
      [
       "General Use",
       "General lighting"
      ],
      [
       "Light source",
       "LED"
      ]
     ]
    },
    {
     "id": "led_batten_light",
     "name": "LED Batten Light",
     "description": "LED batten light for general lighting.",
     "specs": [
      [
       "Product Type",
       "LED luminaire"
      ],
      [
       "General Use",
       "General lighting"
      ],
      [
       "Light source",
       "LED"
      ]
     ]
    },
    {
     "id": "weatherproof_led_linear_light",
     "name": "Weatherproof LED Linear Light",
     "description": "Weatherproof LED linear light.",
     "specs": [
      [
       "Product Type",
       "LED luminaire"
      ],
      [
       "General Use",
       "Linear lighting"
      ],
      [
       "Light source",
       "LED"
      ]
     ]
    },
    {
     "id": "emergency_bulkhead_light",
     "name": "Emergency Bulkhead Light",
     "description": "Bulkhead light for emergency lighting.",
     "specs": [
      [
       "Product Type",
       "Emergency luminaire"
      ],
      [
       "General Use",
       "Emergency lighting"
      ]
     ]
    },
    {
     "id": "portable_led_work_light",
     "name": "Portable LED Work Light",
     "description": "Portable LED light for work areas.",
     "specs": [
      [
       "Product Type",
       "Portable luminaire"
      ],
      [
       "General Use",
       "Work-area lighting"
      ],
      [
       "Light source",
       "LED"
      ]
     ]
    }
   ]
  },
  {
   "key": "conduits-cable-trays-wiring-accessories",
   "label": "Conduits, Cable Trays & Wiring Accessories",
   "icon": "fa-grip-lines",
   "intro": "Conduits, cable trays and accessories for routing and organising electrical wiring.",
   "products": [
    {
     "id": "rigid_pvc_electrical_conduit",
     "name": "Rigid PVC Electrical Conduit",
     "description": "Rigid PVC conduit for routing electrical wiring.",
     "specs": [
      [
       "Product Type",
       "Conduit"
      ],
      [
       "General Use",
       "Wiring protection"
      ],
      [
       "Material",
       "PVC"
      ]
     ]
    },
    {
     "id": "flexible_corrugated_conduit",
     "name": "Flexible Corrugated Conduit",
     "description": "Flexible corrugated conduit for routing wiring.",
     "specs": [
      [
       "Product Type",
       "Conduit"
      ],
      [
       "General Use",
       "Wiring protection"
      ],
      [
       "Design",
       "Flexible, corrugated"
      ]
     ]
    },
    {
     "id": "gi_electrical_conduit",
     "name": "GI Electrical Conduit",
     "description": "GI conduit for routing electrical wiring.",
     "specs": [
      [
       "Product Type",
       "Conduit"
      ],
      [
       "General Use",
       "Wiring protection"
      ],
      [
       "Material",
       "GI"
      ]
     ]
    },
    {
     "id": "flexible_metallic_conduit",
     "name": "Flexible Metallic Conduit",
     "description": "Flexible metallic conduit for routing wiring.",
     "specs": [
      [
       "Product Type",
       "Conduit"
      ],
      [
       "General Use",
       "Wiring protection"
      ],
      [
       "Material",
       "Metallic"
      ]
     ]
    },
    {
     "id": "perforated_cable_tray",
     "name": "Perforated Cable Tray",
     "description": "Perforated tray for supporting and routing cables.",
     "specs": [
      [
       "Product Type",
       "Cable tray"
      ],
      [
       "General Use",
       "Cable support"
      ],
      [
       "Design",
       "Perforated"
      ]
     ]
    },
    {
     "id": "ladder_cable_tray",
     "name": "Ladder Cable Tray",
     "description": "Ladder-type tray for supporting and routing cables.",
     "specs": [
      [
       "Product Type",
       "Cable tray"
      ],
      [
       "General Use",
       "Cable support"
      ],
      [
       "Design",
       "Ladder type"
      ]
     ]
    },
    {
     "id": "cable_gland",
     "name": "Cable Gland",
     "description": "Gland for securing cables at entry points.",
     "specs": [
      [
       "Product Type",
       "Cable gland"
      ],
      [
       "General Use",
       "Cable entry"
      ]
     ]
    },
    {
     "id": "copper_cable_lug",
     "name": "Copper Cable Lug",
     "description": "Copper lug for terminating cable ends.",
     "specs": [
      [
       "Product Type",
       "Cable lug"
      ],
      [
       "General Use",
       "Cable termination"
      ],
      [
       "Material",
       "Copper"
      ]
     ]
    },
    {
     "id": "nylon_cable_tie",
     "name": "Nylon Cable Tie",
     "description": "Nylon tie for bundling and securing cables.",
     "specs": [
      [
       "Product Type",
       "Cable tie"
      ],
      [
       "General Use",
       "Cable bundling"
      ],
      [
       "Material",
       "Nylon"
      ]
     ]
    }
   ]
  }
 ],
 "electronics": [
  {
   "key": "resistors-capacitors-inductors",
   "label": "Resistors, Capacitors & Inductors",
   "icon": "fa-microchip",
   "intro": "Passive components for circuit design, repair and prototyping.",
   "products": [
    {
     "id": "metal_film_resistor",
     "name": "Metal Film Resistor",
     "description": "Metal film resistor for electronic circuits.",
     "specs": [
      [
       "Product Type",
       "Resistor"
      ],
      [
       "General Use",
       "Electronic circuits"
      ],
      [
       "Technology",
       "Metal film"
      ]
     ]
    },
    {
     "id": "wirewound_power_resistor",
     "name": "Wirewound Power Resistor",
     "description": "Wirewound resistor for power applications.",
     "specs": [
      [
       "Product Type",
       "Resistor"
      ],
      [
       "General Use",
       "Power circuits"
      ],
      [
       "Construction",
       "Wirewound"
      ]
     ]
    },
    {
     "id": "smd_chip_resistor",
     "name": "SMD Chip Resistor",
     "description": "Surface-mount chip resistor for PCB assembly.",
     "specs": [
      [
       "Product Type",
       "Resistor"
      ],
      [
       "General Use",
       "PCB assembly"
      ],
      [
       "Mounting",
       "SMD"
      ]
     ]
    },
    {
     "id": "multiturn_trimmer_potentiometer",
     "name": "Multiturn Trimmer Potentiometer",
     "description": "Multiturn trimmer for adjustable resistance.",
     "specs": [
      [
       "Product Type",
       "Potentiometer"
      ],
      [
       "General Use",
       "Adjustment and calibration"
      ],
      [
       "Type",
       "Multiturn trimmer"
      ]
     ]
    },
    {
     "id": "aluminium_electrolytic_capacitor",
     "name": "Aluminium Electrolytic Capacitor",
     "description": "Aluminium electrolytic capacitor for filtering and energy storage.",
     "specs": [
      [
       "Product Type",
       "Capacitor"
      ],
      [
       "General Use",
       "Filtering and storage"
      ]
     ]
    },
    {
     "id": "ceramic_disc_capacitor",
     "name": "Ceramic Disc Capacitor",
     "description": "Ceramic disc capacitor for electronic circuits.",
     "specs": [
      [
       "Product Type",
       "Capacitor"
      ],
      [
       "General Use",
       "Electronic circuits"
      ],
      [
       "Dielectric",
       "Ceramic"
      ]
     ]
    },
    {
     "id": "smd_multilayer_ceramic_capacitor",
     "name": "SMD Multilayer Ceramic Capacitor",
     "description": "Surface-mount multilayer ceramic capacitor.",
     "specs": [
      [
       "Product Type",
       "Capacitor"
      ],
      [
       "General Use",
       "PCB assembly"
      ],
      [
       "Mounting",
       "SMD"
      ]
     ]
    },
    {
     "id": "film_capacitor",
     "name": "Film Capacitor",
     "description": "Film capacitor for electronic and electrical circuits.",
     "specs": [
      [
       "Product Type",
       "Capacitor"
      ],
      [
       "General Use",
       "Circuit use"
      ]
     ]
    },
    {
     "id": "radial_power_inductor",
     "name": "Radial Power Inductor",
     "description": "Radial power inductor for energy storage and filtering.",
     "specs": [
      [
       "Product Type",
       "Inductor"
      ],
      [
       "General Use",
       "Power and filtering circuits"
      ],
      [
       "Lead style",
       "Radial"
      ]
     ]
    }
   ]
  },
  {
   "key": "diodes-transistors-integrated-circuits",
   "label": "Diodes, Transistors & Integrated Circuits",
   "icon": "fa-memory",
   "intro": "Discrete semiconductors and integrated circuits for switching, amplification and control.",
   "products": [
    {
     "id": "rectifier_diode",
     "name": "Rectifier Diode",
     "description": "Diode used for rectification.",
     "specs": [
      [
       "Product Type",
       "Diode"
      ],
      [
       "General Use",
       "Rectification"
      ]
     ]
    },
    {
     "id": "zener_diode",
     "name": "Zener Diode",
     "description": "Zener diode used for voltage regulation and reference.",
     "specs": [
      [
       "Product Type",
       "Diode"
      ],
      [
       "General Use",
       "Voltage regulation"
      ]
     ]
    },
    {
     "id": "schottky_diode",
     "name": "Schottky Diode",
     "description": "Schottky diode for switching and rectification.",
     "specs": [
      [
       "Product Type",
       "Diode"
      ],
      [
       "General Use",
       "Switching and rectification"
      ]
     ]
    },
    {
     "id": "bridge_rectifier",
     "name": "Bridge Rectifier",
     "description": "Bridge rectifier for converting AC to DC.",
     "specs": [
      [
       "Product Type",
       "Rectifier"
      ],
      [
       "General Use",
       "AC to DC conversion"
      ]
     ]
    },
    {
     "id": "bipolar_junction_transistor",
     "name": "Bipolar Junction Transistor",
     "description": "Bipolar junction transistor for amplification and switching.",
     "specs": [
      [
       "Product Type",
       "Transistor"
      ],
      [
       "General Use",
       "Amplification and switching"
      ]
     ]
    },
    {
     "id": "power_mosfet",
     "name": "Power MOSFET",
     "description": "Power MOSFET for switching applications.",
     "specs": [
      [
       "Product Type",
       "Transistor"
      ],
      [
       "General Use",
       "Power switching"
      ]
     ]
    },
    {
     "id": "igbt",
     "name": "IGBT",
     "description": "IGBT for power switching applications.",
     "specs": [
      [
       "Product Type",
       "Power transistor"
      ],
      [
       "General Use",
       "Power switching"
      ]
     ]
    },
    {
     "id": "operational_amplifier_ic",
     "name": "Operational Amplifier IC",
     "description": "Operational amplifier IC for signal amplification.",
     "specs": [
      [
       "Product Type",
       "Integrated circuit"
      ],
      [
       "General Use",
       "Signal amplification"
      ]
     ]
    },
    {
     "id": "optocoupler_ic",
     "name": "Optocoupler IC",
     "description": "Optocoupler IC for signal isolation between circuits.",
     "specs": [
      [
       "Product Type",
       "Integrated circuit"
      ],
      [
       "General Use",
       "Signal isolation"
      ]
     ]
    }
   ]
  },
  {
   "key": "relays-switches-electromechanical-components",
   "label": "Relays, Switches & Electromechanical Components",
   "icon": "fa-toggle-on",
   "intro": "Relays, switches and other electromechanical parts for electronic and control circuits.",
   "products": [
    {
     "id": "pcb_mounted_electromagnetic_relay",
     "name": "PCB-Mounted Electromagnetic Relay",
     "description": "Electromagnetic relay for PCB mounting.",
     "specs": [
      [
       "Product Type",
       "Relay"
      ],
      [
       "General Use",
       "Switching control"
      ],
      [
       "Mounting",
       "PCB"
      ]
     ]
    },
    {
     "id": "plug_in_electromagnetic_relay",
     "name": "Plug-In Electromagnetic Relay",
     "description": "Electromagnetic relay for plug-in mounting.",
     "specs": [
      [
       "Product Type",
       "Relay"
      ],
      [
       "General Use",
       "Switching control"
      ],
      [
       "Mounting",
       "Plug-in"
      ]
     ]
    },
    {
     "id": "panel_mounted_solid_state_relay",
     "name": "Panel-Mounted Solid-State Relay",
     "description": "Solid-state relay for panel mounting.",
     "specs": [
      [
       "Product Type",
       "Relay"
      ],
      [
       "General Use",
       "Switching control"
      ],
      [
       "Mounting",
       "Panel"
      ]
     ]
    },
    {
     "id": "microswitch",
     "name": "Microswitch",
     "description": "Microswitch for switching on mechanical actuation.",
     "specs": [
      [
       "Product Type",
       "Switch"
      ],
      [
       "General Use",
       "Position and limit switching"
      ]
     ]
    },
    {
     "id": "rocker_switch",
     "name": "Rocker Switch",
     "description": "Rocker switch for on/off switching.",
     "specs": [
      [
       "Product Type",
       "Switch"
      ],
      [
       "General Use",
       "On/off switching"
      ]
     ]
    },
    {
     "id": "tactile_pushbutton_switch",
     "name": "Tactile Pushbutton Switch",
     "description": "Tactile pushbutton switch for momentary input.",
     "specs": [
      [
       "Product Type",
       "Switch"
      ],
      [
       "General Use",
       "Momentary input"
      ]
     ]
    },
    {
     "id": "dip_switch",
     "name": "DIP Switch",
     "description": "DIP switch for configuration settings.",
     "specs": [
      [
       "Product Type",
       "Switch"
      ],
      [
       "General Use",
       "Configuration settings"
      ]
     ]
    },
    {
     "id": "electromagnetic_buzzer",
     "name": "Electromagnetic Buzzer",
     "description": "Electromagnetic buzzer for audible signalling.",
     "specs": [
      [
       "Product Type",
       "Buzzer"
      ],
      [
       "General Use",
       "Audible signalling"
      ]
     ]
    },
    {
     "id": "dc_axial_cooling_fan",
     "name": "DC Axial Cooling Fan",
     "description": "DC axial fan for airflow and cooling.",
     "specs": [
      [
       "Product Type",
       "Cooling fan"
      ],
      [
       "General Use",
       "Equipment cooling"
      ],
      [
       "Supply",
       "DC"
      ]
     ]
    }
   ]
  },
  {
   "key": "connectors-terminal-blocks-cable-assemblies",
   "label": "Connectors, Terminal Blocks & Cable Assemblies",
   "icon": "fa-plug",
   "intro": "Connectors, terminal blocks and cable assemblies for joining boards, wires and equipment.",
   "products": [
    {
     "id": "pcb_screw_terminal_block",
     "name": "PCB Screw Terminal Block",
     "description": "Screw terminal block for PCB mounting.",
     "specs": [
      [
       "Product Type",
       "Terminal block"
      ],
      [
       "General Use",
       "PCB wiring"
      ],
      [
       "Mounting",
       "PCB"
      ]
     ]
    },
    {
     "id": "pluggable_pcb_terminal_block",
     "name": "Pluggable PCB Terminal Block",
     "description": "Pluggable terminal block for PCB connections.",
     "specs": [
      [
       "Product Type",
       "Terminal block"
      ],
      [
       "General Use",
       "PCB wiring"
      ],
      [
       "Type",
       "Pluggable"
      ]
     ]
    },
    {
     "id": "din_rail_feed_through_terminal_block",
     "name": "DIN-Rail Feed-Through Terminal Block",
     "description": "Feed-through terminal block for DIN-rail mounting.",
     "specs": [
      [
       "Product Type",
       "Terminal block"
      ],
      [
       "General Use",
       "Wire connections"
      ],
      [
       "Mounting",
       "DIN rail"
      ]
     ]
    },
    {
     "id": "male_female_pin_header_set",
     "name": "Male & Female Pin Header Set",
     "description": "Set of male and female pin headers.",
     "specs": [
      [
       "Product Type",
       "Header set"
      ],
      [
       "General Use",
       "Board connections"
      ]
     ]
    },
    {
     "id": "idc_ribbon_cable_assembly",
     "name": "IDC Ribbon Cable Assembly",
     "description": "Ribbon cable assembly with IDC connectors.",
     "specs": [
      [
       "Product Type",
       "Cable assembly"
      ],
      [
       "General Use",
       "Board connections"
      ]
     ]
    },
    {
     "id": "d_sub_connector",
     "name": "D-Sub Connector",
     "description": "D-Sub connector for signal and data connections.",
     "specs": [
      [
       "Product Type",
       "Connector"
      ],
      [
       "General Use",
       "Signal and data connections"
      ]
     ]
    },
    {
     "id": "circular_industrial_connector",
     "name": "Circular Industrial Connector",
     "description": "Circular connector for industrial connections.",
     "specs": [
      [
       "Product Type",
       "Connector"
      ],
      [
       "General Use",
       "Industrial connections"
      ],
      [
       "Shape",
       "Circular"
      ]
     ]
    },
    {
     "id": "rj45_ethernet_patch_cable",
     "name": "RJ45 Ethernet Patch Cable",
     "description": "Ethernet patch cable with RJ45 connectors.",
     "specs": [
      [
       "Product Type",
       "Patch cable"
      ],
      [
       "General Use",
       "Network connections"
      ],
      [
       "Connector",
       "RJ45"
      ]
     ]
    },
    {
     "id": "board_to_wire_crimp_connector_set",
     "name": "Board-to-Wire Crimp Connector Set",
     "description": "Crimp connector set for board-to-wire connections.",
     "specs": [
      [
       "Product Type",
       "Connector set"
      ],
      [
       "General Use",
       "Board-to-wire connections"
      ],
      [
       "Termination",
       "Crimp"
      ]
     ]
    }
   ]
  },
  {
   "key": "sensors-control-modules",
   "label": "Sensors & Control Modules",
   "icon": "fa-sliders",
   "intro": "Sensors and control modules for measurement, monitoring and automation projects.",
   "products": [
    {
     "id": "inductive_proximity_sensor",
     "name": "Inductive Proximity Sensor",
     "description": "Proximity sensor using inductive sensing.",
     "specs": [
      [
       "Product Type",
       "Proximity sensor"
      ],
      [
       "General Use",
       "Object detection"
      ],
      [
       "Sensing",
       "Inductive"
      ]
     ]
    },
    {
     "id": "capacitive_proximity_sensor",
     "name": "Capacitive Proximity Sensor",
     "description": "Proximity sensor using capacitive sensing.",
     "specs": [
      [
       "Product Type",
       "Proximity sensor"
      ],
      [
       "General Use",
       "Object detection"
      ],
      [
       "Sensing",
       "Capacitive"
      ]
     ]
    },
    {
     "id": "photoelectric_sensor",
     "name": "Photoelectric Sensor",
     "description": "Sensor using light for object detection.",
     "specs": [
      [
       "Product Type",
       "Optical sensor"
      ],
      [
       "General Use",
       "Object detection"
      ],
      [
       "Sensing",
       "Photoelectric"
      ]
     ]
    },
    {
     "id": "magnetic_reed_sensor",
     "name": "Magnetic Reed Sensor",
     "description": "Reed sensor that responds to a magnetic field.",
     "specs": [
      [
       "Product Type",
       "Magnetic sensor"
      ],
      [
       "General Use",
       "Magnetic detection"
      ],
      [
       "Type",
       "Reed"
      ]
     ]
    },
    {
     "id": "rotary_encoder",
     "name": "Rotary Encoder",
     "description": "Encoder for rotary position or speed feedback.",
     "specs": [
      [
       "Product Type",
       "Encoder"
      ],
      [
       "General Use",
       "Position and speed feedback"
      ],
      [
       "Motion",
       "Rotary"
      ]
     ]
    },
    {
     "id": "thermocouple_probe",
     "name": "Thermocouple Probe",
     "description": "Probe using a thermocouple for temperature measurement.",
     "specs": [
      [
       "Product Type",
       "Temperature probe"
      ],
      [
       "General Use",
       "Temperature measurement"
      ],
      [
       "Sensing",
       "Thermocouple"
      ]
     ]
    },
    {
     "id": "pt100_rtd_probe",
     "name": "PT100 RTD Probe",
     "description": "RTD probe with a PT100 element for temperature measurement.",
     "specs": [
      [
       "Product Type",
       "Temperature probe"
      ],
      [
       "General Use",
       "Temperature measurement"
      ],
      [
       "Element",
       "PT100"
      ]
     ]
    },
    {
     "id": "digital_temperature_controller",
     "name": "Digital Temperature Controller",
     "description": "Digital controller for temperature control.",
     "specs": [
      [
       "Product Type",
       "Controller"
      ],
      [
       "General Use",
       "Temperature control"
      ],
      [
       "Display",
       "Digital"
      ]
     ]
    },
    {
     "id": "digital_timer_controller",
     "name": "Digital Timer Controller",
     "description": "Digital timer controller for timed switching.",
     "specs": [
      [
       "Product Type",
       "Controller"
      ],
      [
       "General Use",
       "Timed control"
      ],
      [
       "Display",
       "Digital"
      ]
     ]
    }
   ]
  },
  {
   "key": "power-supplies-dc-converters",
   "label": "Power Supplies & DC Converters",
   "icon": "fa-battery-full",
   "intro": "Power supplies and DC converters for powering electronic equipment and circuits.",
   "products": [
    {
     "id": "din_rail_acdc_power_supply",
     "name": "DIN-Rail AC–DC Power Supply",
     "description": "AC–DC power supply for DIN-rail mounting.",
     "specs": [
      [
       "Product Type",
       "Power supply"
      ],
      [
       "General Use",
       "DC power"
      ],
      [
       "Mounting",
       "DIN rail"
      ]
     ]
    },
    {
     "id": "enclosed_metal_acdc_switching_power_supply",
     "name": "Enclosed Metal AC–DC Switching Power Supply",
     "description": "Enclosed metal AC–DC switching power supply.",
     "specs": [
      [
       "Product Type",
       "Power supply"
      ],
      [
       "General Use",
       "DC power"
      ],
      [
       "Housing",
       "Enclosed metal"
      ]
     ]
    },
    {
     "id": "open_frame_acdc_power_supply",
     "name": "Open-Frame AC–DC Power Supply",
     "description": "Open-frame AC–DC power supply.",
     "specs": [
      [
       "Product Type",
       "Power supply"
      ],
      [
       "General Use",
       "DC power"
      ],
      [
       "Housing",
       "Open frame"
      ]
     ]
    },
    {
     "id": "desktop_acdc_adapter",
     "name": "Desktop AC–DC Adapter",
     "description": "Desktop AC–DC adapter for powering devices.",
     "specs": [
      [
       "Product Type",
       "Power adapter"
      ],
      [
       "General Use",
       "Device power"
      ],
      [
       "Format",
       "Desktop"
      ]
     ]
    },
    {
     "id": "pcb_mounted_acdc_power_module",
     "name": "PCB-Mounted AC–DC Power Module",
     "description": "AC–DC power module for PCB mounting.",
     "specs": [
      [
       "Product Type",
       "Power module"
      ],
      [
       "General Use",
       "DC power"
      ],
      [
       "Mounting",
       "PCB"
      ]
     ]
    },
    {
     "id": "dcdc_buck_converter_module",
     "name": "DC–DC Buck Converter Module",
     "description": "DC–DC buck converter module for stepping voltage down.",
     "specs": [
      [
       "Product Type",
       "DC–DC converter"
      ],
      [
       "General Use",
       "Voltage step-down"
      ],
      [
       "Function",
       "Buck"
      ]
     ]
    },
    {
     "id": "dcdc_boost_converter_module",
     "name": "DC–DC Boost Converter Module",
     "description": "DC–DC boost converter module for stepping voltage up.",
     "specs": [
      [
       "Product Type",
       "DC–DC converter"
      ],
      [
       "General Use",
       "Voltage step-up"
      ],
      [
       "Function",
       "Boost"
      ]
     ]
    },
    {
     "id": "isolated_dcdc_converter_module",
     "name": "Isolated DC–DC Converter Module",
     "description": "Isolated DC–DC converter module.",
     "specs": [
      [
       "Product Type",
       "DC–DC converter"
      ],
      [
       "General Use",
       "DC conversion"
      ],
      [
       "Type",
       "Isolated"
      ]
     ]
    },
    {
     "id": "din_rail_dc_ups_module",
     "name": "DIN-Rail DC UPS Module",
     "description": "DC UPS module for DIN-rail mounting.",
     "specs": [
      [
       "Product Type",
       "DC UPS module"
      ],
      [
       "General Use",
       "DC backup power"
      ],
      [
       "Mounting",
       "DIN rail"
      ]
     ]
    }
   ]
  },
  {
   "key": "circuit-protection-pcb-accessories",
   "label": "Circuit Protection & PCB Accessories",
   "icon": "fa-shield-halved",
   "intro": "Fuses and protection devices, with accessories for building and mounting circuit boards.",
   "products": [
    {
     "id": "glass_cartridge_fuse",
     "name": "Glass Cartridge Fuse",
     "description": "Cartridge fuse with a glass body for circuit protection.",
     "specs": [
      [
       "Product Type",
       "Fuse"
      ],
      [
       "General Use",
       "Circuit protection"
      ],
      [
       "Body",
       "Glass"
      ]
     ]
    },
    {
     "id": "ceramic_cartridge_fuse",
     "name": "Ceramic Cartridge Fuse",
     "description": "Cartridge fuse with a ceramic body for circuit protection.",
     "specs": [
      [
       "Product Type",
       "Fuse"
      ],
      [
       "General Use",
       "Circuit protection"
      ],
      [
       "Body",
       "Ceramic"
      ]
     ]
    },
    {
     "id": "pcb_fuse_holder",
     "name": "PCB Fuse Holder",
     "description": "Fuse holder for PCB mounting.",
     "specs": [
      [
       "Product Type",
       "Fuse holder"
      ],
      [
       "General Use",
       "Fuse mounting"
      ],
      [
       "Mounting",
       "PCB"
      ]
     ]
    },
    {
     "id": "resettable_ptc_fuse",
     "name": "Resettable PTC Fuse",
     "description": "Resettable PTC fuse for overcurrent protection.",
     "specs": [
      [
       "Product Type",
       "Fuse"
      ],
      [
       "General Use",
       "Overcurrent protection"
      ],
      [
       "Type",
       "Resettable PTC"
      ]
     ]
    },
    {
     "id": "metal_oxide_varistor",
     "name": "Metal Oxide Varistor",
     "description": "Metal oxide varistor for surge suppression.",
     "specs": [
      [
       "Product Type",
       "Varistor"
      ],
      [
       "General Use",
       "Surge suppression"
      ]
     ]
    },
    {
     "id": "tvs_diode",
     "name": "TVS Diode",
     "description": "TVS diode for transient voltage suppression.",
     "specs": [
      [
       "Product Type",
       "Diode"
      ],
      [
       "General Use",
       "Transient suppression"
      ]
     ]
    },
    {
     "id": "ntc_inrush_current_limiter",
     "name": "NTC Inrush Current Limiter",
     "description": "NTC thermistor for limiting inrush current.",
     "specs": [
      [
       "Product Type",
       "Thermistor"
      ],
      [
       "General Use",
       "Inrush current limiting"
      ],
      [
       "Type",
       "NTC"
      ]
     ]
    },
    {
     "id": "pcb_mounting_spacer_set",
     "name": "PCB Mounting Spacer Set",
     "description": "Spacer set for mounting PCBs.",
     "specs": [
      [
       "Product Type",
       "Spacer set"
      ],
      [
       "General Use",
       "PCB mounting"
      ]
     ]
    },
    {
     "id": "electronic_component_heat_sink",
     "name": "Electronic Component Heat Sink",
     "description": "Heat sink for electronic components.",
     "specs": [
      [
       "Product Type",
       "Heat sink"
      ],
      [
       "General Use",
       "Heat dissipation"
      ]
     ]
    }
   ]
  }
 ],
 "hardwares": [
  {
   "key": "fasteners-anchors",
   "label": "Fasteners & Anchors",
   "icon": "fa-screwdriver",
   "intro": "Bolts, nuts, screws, rivets and anchors for fixing and joining.",
   "products": [
    {
     "id": "hex_head_bolt",
     "name": "Hex Head Bolt",
     "description": "Bolt with a hex head for fastening.",
     "specs": [
      [
       "Product Type",
       "Bolt"
      ],
      [
       "General Use",
       "Fastening"
      ],
      [
       "Head",
       "Hex"
      ]
     ]
    },
    {
     "id": "socket_head_cap_screw",
     "name": "Socket Head Cap Screw",
     "description": "Cap screw with a socket head.",
     "specs": [
      [
       "Product Type",
       "Screw"
      ],
      [
       "General Use",
       "Fastening"
      ],
      [
       "Head",
       "Socket"
      ]
     ]
    },
    {
     "id": "hex_nut",
     "name": "Hex Nut",
     "description": "Hex nut for use with bolts.",
     "specs": [
      [
       "Product Type",
       "Nut"
      ],
      [
       "General Use",
       "Fastening"
      ],
      [
       "Shape",
       "Hex"
      ]
     ]
    },
    {
     "id": "nylon_insert_lock_nut",
     "name": "Nylon Insert Lock Nut",
     "description": "Lock nut with a nylon insert.",
     "specs": [
      [
       "Product Type",
       "Lock nut"
      ],
      [
       "General Use",
       "Fastening"
      ],
      [
       "Locking",
       "Nylon insert"
      ]
     ]
    },
    {
     "id": "flat_washer",
     "name": "Flat Washer",
     "description": "Flat washer for use with fasteners.",
     "specs": [
      [
       "Product Type",
       "Washer"
      ],
      [
       "General Use",
       "Fastening"
      ],
      [
       "Shape",
       "Flat"
      ]
     ]
    },
    {
     "id": "spring_washer",
     "name": "Spring Washer",
     "description": "Spring washer for use with fasteners.",
     "specs": [
      [
       "Product Type",
       "Washer"
      ],
      [
       "General Use",
       "Fastening"
      ],
      [
       "Type",
       "Spring"
      ]
     ]
    },
    {
     "id": "self_drilling_screw",
     "name": "Self-Drilling Screw",
     "description": "Screw that drills its own hole while fastening.",
     "specs": [
      [
       "Product Type",
       "Screw"
      ],
      [
       "General Use",
       "Fastening"
      ],
      [
       "Type",
       "Self-drilling"
      ]
     ]
    },
    {
     "id": "blind_rivet",
     "name": "Blind Rivet",
     "description": "Rivet for joining from one side.",
     "specs": [
      [
       "Product Type",
       "Rivet"
      ],
      [
       "General Use",
       "Joining"
      ],
      [
       "Type",
       "Blind"
      ]
     ]
    },
    {
     "id": "wedge_anchor",
     "name": "Wedge Anchor",
     "description": "Wedge anchor for fastening to a solid base.",
     "specs": [
      [
       "Product Type",
       "Anchor"
      ],
      [
       "General Use",
       "Anchoring"
      ],
      [
       "Type",
       "Wedge"
      ]
     ]
    }
   ]
  },
  {
   "key": "hand-tools",
   "label": "Hand Tools",
   "icon": "fa-wrench",
   "intro": "Hand tools for construction, installation, maintenance and workshop tasks.",
   "products": [
    {
     "id": "combination_spanner",
     "name": "Combination Spanner",
     "description": "Spanner with open and ring ends.",
     "specs": [
      [
       "Product Type",
       "Spanner"
      ],
      [
       "General Use",
       "Tightening and loosening"
      ],
      [
       "Ends",
       "Open and ring"
      ]
     ]
    },
    {
     "id": "adjustable_spanner",
     "name": "Adjustable Spanner",
     "description": "Spanner with an adjustable jaw.",
     "specs": [
      [
       "Product Type",
       "Spanner"
      ],
      [
       "General Use",
       "Tightening and loosening"
      ],
      [
       "Jaw",
       "Adjustable"
      ]
     ]
    },
    {
     "id": "socket_wrench_set",
     "name": "Socket Wrench Set",
     "description": "Set of sockets with a wrench for fasteners.",
     "specs": [
      [
       "Product Type",
       "Wrench set"
      ],
      [
       "General Use",
       "Tightening and loosening"
      ]
     ]
    },
    {
     "id": "combination_pliers",
     "name": "Combination Pliers",
     "description": "Combination pliers for gripping and holding.",
     "specs": [
      [
       "Product Type",
       "Pliers"
      ],
      [
       "General Use",
       "Gripping"
      ]
     ]
    },
    {
     "id": "long_nose_pliers",
     "name": "Long-Nose Pliers",
     "description": "Long-nose pliers for gripping in narrow spaces.",
     "specs": [
      [
       "Product Type",
       "Pliers"
      ],
      [
       "General Use",
       "Gripping"
      ],
      [
       "Jaws",
       "Long-nose"
      ]
     ]
    },
    {
     "id": "screwdriver_set",
     "name": "Screwdriver Set",
     "description": "Set of screwdrivers for driving screws.",
     "specs": [
      [
       "Product Type",
       "Screwdriver set"
      ],
      [
       "General Use",
       "Screw driving"
      ]
     ]
    },
    {
     "id": "hex_key_set",
     "name": "Hex Key Set",
     "description": "Set of hex keys for hex-socket fasteners.",
     "specs": [
      [
       "Product Type",
       "Key set"
      ],
      [
       "General Use",
       "Screw driving"
      ]
     ]
    },
    {
     "id": "ball_peen_hammer",
     "name": "Ball-Peen Hammer",
     "description": "Hammer with a ball peen.",
     "specs": [
      [
       "Product Type",
       "Hammer"
      ],
      [
       "General Use",
       "Striking"
      ],
      [
       "Head",
       "Ball peen"
      ]
     ]
    },
    {
     "id": "torque_wrench",
     "name": "Torque Wrench",
     "description": "Wrench for tightening to a set torque.",
     "specs": [
      [
       "Product Type",
       "Wrench"
      ],
      [
       "General Use",
       "Controlled tightening"
      ]
     ]
    }
   ]
  },
  {
   "key": "power-tools-accessories",
   "label": "Power Tools & Accessories",
   "icon": "fa-gear",
   "intro": "Corded and cordless power tools with accessories for drilling, grinding and fastening.",
   "products": [
    {
     "id": "corded_impact_drill",
     "name": "Corded Impact Drill",
     "description": "Corded drill with impact action.",
     "specs": [
      [
       "Product Type",
       "Power drill"
      ],
      [
       "General Use",
       "Drilling"
      ],
      [
       "Power",
       "Corded"
      ]
     ]
    },
    {
     "id": "cordless_drill_driver",
     "name": "Cordless Drill Driver",
     "description": "Cordless drill driver for drilling and driving screws.",
     "specs": [
      [
       "Product Type",
       "Power drill"
      ],
      [
       "General Use",
       "Drilling and driving"
      ],
      [
       "Power",
       "Cordless"
      ]
     ]
    },
    {
     "id": "rotary_hammer_drill",
     "name": "Rotary Hammer Drill",
     "description": "Rotary hammer drill for drilling.",
     "specs": [
      [
       "Product Type",
       "Power drill"
      ],
      [
       "General Use",
       "Drilling"
      ],
      [
       "Type",
       "Rotary hammer"
      ]
     ]
    },
    {
     "id": "angle_grinder",
     "name": "Angle Grinder",
     "description": "Angle grinder for cutting and grinding.",
     "specs": [
      [
       "Product Type",
       "Grinder"
      ],
      [
       "General Use",
       "Cutting and grinding"
      ]
     ]
    },
    {
     "id": "die_grinder",
     "name": "Die Grinder",
     "description": "Die grinder for grinding and finishing.",
     "specs": [
      [
       "Product Type",
       "Grinder"
      ],
      [
       "General Use",
       "Grinding and finishing"
      ]
     ]
    },
    {
     "id": "electric_impact_wrench",
     "name": "Electric Impact Wrench",
     "description": "Electric wrench with impact action for fasteners.",
     "specs": [
      [
       "Product Type",
       "Impact wrench"
      ],
      [
       "General Use",
       "Tightening and loosening"
      ],
      [
       "Power",
       "Electric"
      ]
     ]
    },
    {
     "id": "cut_off_saw",
     "name": "Cut-Off Saw",
     "description": "Saw for cutting off material.",
     "specs": [
      [
       "Product Type",
       "Saw"
      ],
      [
       "General Use",
       "Cutting"
      ]
     ]
    },
    {
     "id": "heat_gun",
     "name": "Heat Gun",
     "description": "Heat gun for applying hot air.",
     "specs": [
      [
       "Product Type",
       "Heating tool"
      ],
      [
       "General Use",
       "Heating"
      ]
     ]
    },
    {
     "id": "power_tool_battery_charger_set",
     "name": "Power Tool Battery & Charger Set",
     "description": "Battery and charger set for cordless tools.",
     "specs": [
      [
       "Product Type",
       "Battery set"
      ],
      [
       "General Use",
       "Cordless tool power"
      ]
     ]
    }
   ]
  },
  {
   "key": "cutting-tools-abrasives",
   "label": "Cutting Tools & Abrasives",
   "icon": "fa-scissors",
   "intro": "Cutting tools and abrasives for cutting, grinding, sanding and finishing.",
   "products": [
    {
     "id": "hss_twist_drill_bit_set",
     "name": "HSS Twist Drill Bit Set",
     "description": "Set of HSS twist drill bits.",
     "specs": [
      [
       "Product Type",
       "Drill bit set"
      ],
      [
       "General Use",
       "Drilling"
      ],
      [
       "Material",
       "HSS"
      ]
     ]
    },
    {
     "id": "masonry_drill_bit_set",
     "name": "Masonry Drill Bit Set",
     "description": "Set of drill bits for masonry.",
     "specs": [
      [
       "Product Type",
       "Drill bit set"
      ],
      [
       "General Use",
       "Masonry drilling"
      ]
     ]
    },
    {
     "id": "hole_saw_set",
     "name": "Hole Saw Set",
     "description": "Set of hole saws for cutting round holes.",
     "specs": [
      [
       "Product Type",
       "Hole saw set"
      ],
      [
       "General Use",
       "Hole cutting"
      ]
     ]
    },
    {
     "id": "hand_tap_set",
     "name": "Hand Tap Set",
     "description": "Set of taps for cutting internal threads.",
     "specs": [
      [
       "Product Type",
       "Tap set"
      ],
      [
       "General Use",
       "Thread cutting"
      ],
      [
       "Operation",
       "Hand"
      ]
     ]
    },
    {
     "id": "hacksaw_blade",
     "name": "Hacksaw Blade",
     "description": "Blade for use in a hacksaw.",
     "specs": [
      [
       "Product Type",
       "Saw blade"
      ],
      [
       "General Use",
       "Hand sawing"
      ]
     ]
    },
    {
     "id": "metal_cut_off_disc",
     "name": "Metal Cut-Off Disc",
     "description": "Abrasive disc for cutting metal.",
     "specs": [
      [
       "Product Type",
       "Abrasive disc"
      ],
      [
       "General Use",
       "Metal cutting"
      ]
     ]
    },
    {
     "id": "grinding_disc",
     "name": "Grinding Disc",
     "description": "Abrasive disc for grinding.",
     "specs": [
      [
       "Product Type",
       "Abrasive disc"
      ],
      [
       "General Use",
       "Grinding"
      ]
     ]
    },
    {
     "id": "flap_disc",
     "name": "Flap Disc",
     "description": "Flap disc for grinding and finishing.",
     "specs": [
      [
       "Product Type",
       "Abrasive disc"
      ],
      [
       "General Use",
       "Grinding and finishing"
      ],
      [
       "Type",
       "Flap"
      ]
     ]
    },
    {
     "id": "emery_abrasive_sheet",
     "name": "Emery Abrasive Sheet",
     "description": "Emery abrasive sheet for sanding.",
     "specs": [
      [
       "Product Type",
       "Abrasive sheet"
      ],
      [
       "General Use",
       "Sanding"
      ],
      [
       "Abrasive",
       "Emery"
      ]
     ]
    }
   ]
  },
  {
   "key": "pipes-valves-plumbing-fittings",
   "label": "Pipes, Valves & Plumbing Fittings",
   "icon": "fa-faucet",
   "intro": "Pipes, valves and fittings for water supply, drainage and general plumbing.",
   "products": [
    {
     "id": "gi_threaded_pipe",
     "name": "GI Threaded Pipe",
     "description": "Threaded GI pipe for piping.",
     "specs": [
      [
       "Product Type",
       "Pipe"
      ],
      [
       "General Use",
       "Piping"
      ],
      [
       "Material",
       "GI"
      ]
     ]
    },
    {
     "id": "pvc_pressure_pipe",
     "name": "PVC Pressure Pipe",
     "description": "PVC pipe for pressure piping.",
     "specs": [
      [
       "Product Type",
       "Pipe"
      ],
      [
       "General Use",
       "Pressure piping"
      ],
      [
       "Material",
       "PVC"
      ]
     ]
    },
    {
     "id": "cpvc_pipe",
     "name": "CPVC Pipe",
     "description": "CPVC pipe for piping.",
     "specs": [
      [
       "Product Type",
       "Pipe"
      ],
      [
       "General Use",
       "Piping"
      ],
      [
       "Material",
       "CPVC"
      ]
     ]
    },
    {
     "id": "gi_threaded_elbow",
     "name": "GI Threaded Elbow",
     "description": "Threaded GI elbow for changing pipe direction.",
     "specs": [
      [
       "Product Type",
       "Pipe fitting"
      ],
      [
       "General Use",
       "Direction change"
      ],
      [
       "Material",
       "GI"
      ]
     ]
    },
    {
     "id": "gi_threaded_tee",
     "name": "GI Threaded Tee",
     "description": "Threaded GI tee for branching pipe runs.",
     "specs": [
      [
       "Product Type",
       "Pipe fitting"
      ],
      [
       "General Use",
       "Pipe branching"
      ],
      [
       "Material",
       "GI"
      ]
     ]
    },
    {
     "id": "pipe_union",
     "name": "Pipe Union",
     "description": "Union for joining and disconnecting pipe sections.",
     "specs": [
      [
       "Product Type",
       "Pipe fitting"
      ],
      [
       "General Use",
       "Pipe joining"
      ]
     ]
    },
    {
     "id": "brass_ball_valve",
     "name": "Brass Ball Valve",
     "description": "Brass ball valve for flow shut-off.",
     "specs": [
      [
       "Product Type",
       "Valve"
      ],
      [
       "General Use",
       "Flow shut-off"
      ],
      [
       "Material",
       "Brass"
      ]
     ]
    },
    {
     "id": "gate_valve",
     "name": "Gate Valve",
     "description": "Gate valve for flow isolation.",
     "specs": [
      [
       "Product Type",
       "Valve"
      ],
      [
       "General Use",
       "Flow isolation"
      ]
     ]
    },
    {
     "id": "non_return_valve",
     "name": "Non-Return Valve",
     "description": "Non-return valve for one-way flow.",
     "specs": [
      [
       "Product Type",
       "Valve"
      ],
      [
       "General Use",
       "One-way flow"
      ]
     ]
    }
   ]
  },
  {
   "key": "measuring-inspection-tools",
   "label": "Measuring & Inspection Tools",
   "icon": "fa-ruler",
   "intro": "Tools for measuring, levelling and checking work.",
   "products": [
    {
     "id": "measuring_tape",
     "name": "Measuring Tape",
     "description": "Tape for measuring length.",
     "specs": [
      [
       "Product Type",
       "Measuring tool"
      ],
      [
       "General Use",
       "Length measurement"
      ]
     ]
    },
    {
     "id": "steel_rule",
     "name": "Steel Rule",
     "description": "Steel rule for linear measurement.",
     "specs": [
      [
       "Product Type",
       "Measuring tool"
      ],
      [
       "General Use",
       "Linear measurement"
      ],
      [
       "Material",
       "Steel"
      ]
     ]
    },
    {
     "id": "digital_vernier_caliper",
     "name": "Digital Vernier Caliper",
     "description": "Digital caliper for dimensional measurement.",
     "specs": [
      [
       "Product Type",
       "Measuring instrument"
      ],
      [
       "General Use",
       "Dimensional measurement"
      ],
      [
       "Display",
       "Digital"
      ]
     ]
    },
    {
     "id": "outside_micrometer",
     "name": "Outside Micrometer",
     "description": "Micrometer for measuring outside dimensions.",
     "specs": [
      [
       "Product Type",
       "Measuring instrument"
      ],
      [
       "General Use",
       "Outside measurement"
      ]
     ]
    },
    {
     "id": "dial_indicator",
     "name": "Dial Indicator",
     "description": "Dial indicator for measuring small variations.",
     "specs": [
      [
       "Product Type",
       "Measuring instrument"
      ],
      [
       "General Use",
       "Comparison measurement"
      ],
      [
       "Display",
       "Dial"
      ]
     ]
    },
    {
     "id": "feeler_gauge",
     "name": "Feeler Gauge",
     "description": "Feeler gauge for checking gaps.",
     "specs": [
      [
       "Product Type",
       "Gauge"
      ],
      [
       "General Use",
       "Gap checking"
      ]
     ]
    },
    {
     "id": "thread_pitch_gauge",
     "name": "Thread Pitch Gauge",
     "description": "Gauge for identifying thread pitch.",
     "specs": [
      [
       "Product Type",
       "Gauge"
      ],
      [
       "General Use",
       "Thread checking"
      ]
     ]
    },
    {
     "id": "engineers_try_square",
     "name": "Engineer’s Try Square",
     "description": "Try square for checking right angles.",
     "specs": [
      [
       "Product Type",
       "Square"
      ],
      [
       "General Use",
       "Squareness checking"
      ]
     ]
    },
    {
     "id": "spirit_level",
     "name": "Spirit Level",
     "description": "Spirit level for checking level and plumb.",
     "specs": [
      [
       "Product Type",
       "Level"
      ],
      [
       "General Use",
       "Levelling"
      ]
     ]
    }
   ]
  },
  {
   "key": "hinges-locks-general-hardware",
   "label": "Hinges, Locks & General Hardware",
   "icon": "fa-lock",
   "intro": "Hinges, locks and general hardware for doors, furniture and fittings.",
   "products": [
    {
     "id": "stainless_steel_butt_hinge",
     "name": "Stainless Steel Butt Hinge",
     "description": "Stainless steel butt hinge for hinged joints.",
     "specs": [
      [
       "Product Type",
       "Hinge"
      ],
      [
       "General Use",
       "Hinging"
      ],
      [
       "Material",
       "Stainless steel"
      ]
     ]
    },
    {
     "id": "continuous_piano_hinge",
     "name": "Continuous Piano Hinge",
     "description": "Continuous piano hinge for hinged joints.",
     "specs": [
      [
       "Product Type",
       "Hinge"
      ],
      [
       "General Use",
       "Hinging"
      ],
      [
       "Length",
       "Continuous"
      ]
     ]
    },
    {
     "id": "industrial_padlock",
     "name": "Industrial Padlock",
     "description": "Padlock for securing.",
     "specs": [
      [
       "Product Type",
       "Padlock"
      ],
      [
       "General Use",
       "Securing"
      ]
     ]
    },
    {
     "id": "panel_cam_lock",
     "name": "Panel Cam Lock",
     "description": "Cam lock for panels.",
     "specs": [
      [
       "Product Type",
       "Lock"
      ],
      [
       "General Use",
       "Panel locking"
      ]
     ]
    },
    {
     "id": "toggle_latch",
     "name": "Toggle Latch",
     "description": "Toggle latch for fastening closures.",
     "specs": [
      [
       "Product Type",
       "Latch"
      ],
      [
       "General Use",
       "Fastening"
      ]
     ]
    },
    {
     "id": "barrel_bolt",
     "name": "Barrel Bolt",
     "description": "Barrel bolt for door or gate fastening.",
     "specs": [
      [
       "Product Type",
       "Bolt latch"
      ],
      [
       "General Use",
       "Fastening"
      ]
     ]
    },
    {
     "id": "heavy_duty_drawer_slide",
     "name": "Heavy-Duty Drawer Slide",
     "description": "Drawer slide for sliding drawers.",
     "specs": [
      [
       "Product Type",
       "Drawer slide"
      ],
      [
       "General Use",
       "Drawer mounting"
      ]
     ]
    },
    {
     "id": "industrial_pull_handle",
     "name": "Industrial Pull Handle",
     "description": "Pull handle for doors and panels.",
     "specs": [
      [
       "Product Type",
       "Handle"
      ],
      [
       "General Use",
       "Opening and pulling"
      ]
     ]
    },
    {
     "id": "swivel_castor_wheel",
     "name": "Swivel Castor Wheel",
     "description": "Castor wheel with a swivel mount.",
     "specs": [
      [
       "Product Type",
       "Castor wheel"
      ],
      [
       "General Use",
       "Mobility"
      ],
      [
       "Mount",
       "Swivel"
      ]
     ]
    }
   ]
  }
 ],
 "industrial": [
  {
   "key": "material-handling-storage-equipment",
   "label": "Material Handling & Storage Equipment",
   "icon": "fa-dolly",
   "intro": "Trucks, trolleys and storage equipment for moving and storing materials.",
   "products": [
    {
     "id": "manual_hydraulic_pallet_truck",
     "name": "Manual Hydraulic Pallet Truck",
     "description": "Manual pallet truck with hydraulic lifting.",
     "specs": [
      [
       "Product Type",
       "Pallet truck"
      ],
      [
       "General Use",
       "Pallet moving"
      ],
      [
       "Operation",
       "Manual hydraulic"
      ]
     ]
    },
    {
     "id": "manual_hydraulic_stacker",
     "name": "Manual Hydraulic Stacker",
     "description": "Manual stacker with hydraulic lifting.",
     "specs": [
      [
       "Product Type",
       "Stacker"
      ],
      [
       "General Use",
       "Lifting and stacking"
      ],
      [
       "Operation",
       "Manual hydraulic"
      ]
     ]
    },
    {
     "id": "platform_trolley",
     "name": "Platform Trolley",
     "description": "Platform trolley for moving loads.",
     "specs": [
      [
       "Product Type",
       "Trolley"
      ],
      [
       "General Use",
       "Load moving"
      ]
     ]
    },
    {
     "id": "two_wheel_hand_truck",
     "name": "Two-Wheel Hand Truck",
     "description": "Two-wheel hand truck for moving loads.",
     "specs": [
      [
       "Product Type",
       "Hand truck"
      ],
      [
       "General Use",
       "Load moving"
      ],
      [
       "Wheels",
       "Two"
      ]
     ]
    },
    {
     "id": "manual_chain_pulley_block",
     "name": "Manual Chain Pulley Block",
     "description": "Manual chain pulley block for lifting.",
     "specs": [
      [
       "Product Type",
       "Hoist"
      ],
      [
       "General Use",
       "Lifting"
      ],
      [
       "Operation",
       "Manual"
      ]
     ]
    },
    {
     "id": "lever_hoist",
     "name": "Lever Hoist",
     "description": "Lever-operated hoist for lifting and pulling.",
     "specs": [
      [
       "Product Type",
       "Hoist"
      ],
      [
       "General Use",
       "Lifting and pulling"
      ],
      [
       "Operation",
       "Lever"
      ]
     ]
    },
    {
     "id": "hydraulic_scissor_lift_table",
     "name": "Hydraulic Scissor Lift Table",
     "description": "Scissor lift table with hydraulic lifting.",
     "specs": [
      [
       "Product Type",
       "Lift table"
      ],
      [
       "General Use",
       "Load lifting"
      ],
      [
       "Mechanism",
       "Hydraulic scissor"
      ]
     ]
    },
    {
     "id": "industrial_storage_rack",
     "name": "Industrial Storage Rack",
     "description": "Rack for storing materials.",
     "specs": [
      [
       "Product Type",
       "Storage rack"
      ],
      [
       "General Use",
       "Storage"
      ]
     ]
    },
    {
     "id": "stackable_industrial_storage_bin",
     "name": "Stackable Industrial Storage Bin",
     "description": "Stackable bin for storing parts and materials.",
     "specs": [
      [
       "Product Type",
       "Storage bin"
      ],
      [
       "General Use",
       "Storage"
      ],
      [
       "Design",
       "Stackable"
      ]
     ]
    }
   ]
  },
  {
   "key": "pumps-electric-motors",
   "label": "Pumps & Electric Motors",
   "icon": "fa-gauge-high",
   "intro": "Pumps and electric motors for fluid transfer and mechanical drive applications.",
   "products": [
    {
     "id": "monoblock_centrifugal_pump",
     "name": "Monoblock Centrifugal Pump",
     "description": "Monoblock centrifugal pump for liquid transfer.",
     "specs": [
      [
       "Product Type",
       "Centrifugal pump"
      ],
      [
       "General Use",
       "Liquid transfer"
      ],
      [
       "Construction",
       "Monoblock"
      ]
     ]
    },
    {
     "id": "end_suction_centrifugal_pump",
     "name": "End-Suction Centrifugal Pump",
     "description": "End-suction centrifugal pump for liquid transfer.",
     "specs": [
      [
       "Product Type",
       "Centrifugal pump"
      ],
      [
       "General Use",
       "Liquid transfer"
      ],
      [
       "Design",
       "End-suction"
      ]
     ]
    },
    {
     "id": "submersible_drainage_pump",
     "name": "Submersible Drainage Pump",
     "description": "Submersible pump for drainage.",
     "specs": [
      [
       "Product Type",
       "Submersible pump"
      ],
      [
       "General Use",
       "Drainage"
      ],
      [
       "Installation",
       "Submersible"
      ]
     ]
    },
    {
     "id": "sewage_pump",
     "name": "Sewage Pump",
     "description": "Pump for sewage handling.",
     "specs": [
      [
       "Product Type",
       "Pump"
      ],
      [
       "General Use",
       "Sewage handling"
      ]
     ]
    },
    {
     "id": "multistage_pressure_booster_pump",
     "name": "Multistage Pressure Booster Pump",
     "description": "Multistage pump for boosting pressure.",
     "specs": [
      [
       "Product Type",
       "Booster pump"
      ],
      [
       "General Use",
       "Pressure boosting"
      ],
      [
       "Design",
       "Multistage"
      ]
     ]
    },
    {
     "id": "rotary_gear_pump",
     "name": "Rotary Gear Pump",
     "description": "Rotary gear pump for fluid transfer.",
     "specs": [
      [
       "Product Type",
       "Gear pump"
      ],
      [
       "General Use",
       "Fluid transfer"
      ],
      [
       "Type",
       "Rotary gear"
      ]
     ]
    },
    {
     "id": "three_phase_induction_motor",
     "name": "Three-Phase Induction Motor",
     "description": "Three-phase induction motor for driving machinery.",
     "specs": [
      [
       "Product Type",
       "Electric motor"
      ],
      [
       "General Use",
       "Machine drive"
      ],
      [
       "Supply",
       "Three-phase"
      ]
     ]
    },
    {
     "id": "single_phase_induction_motor",
     "name": "Single-Phase Induction Motor",
     "description": "Single-phase induction motor for driving machinery.",
     "specs": [
      [
       "Product Type",
       "Electric motor"
      ],
      [
       "General Use",
       "Machine drive"
      ],
      [
       "Supply",
       "Single-phase"
      ]
     ]
    },
    {
     "id": "geared_motor",
     "name": "Geared Motor",
     "description": "Motor with an integrated gearbox.",
     "specs": [
      [
       "Product Type",
       "Geared motor"
      ],
      [
       "General Use",
       "Drive applications"
      ]
     ]
    }
   ]
  },
  {
   "key": "pneumatic-hydraulic-components",
   "label": "Pneumatic & Hydraulic Components",
   "icon": "fa-wind",
   "intro": "Pneumatic and hydraulic components for compressed-air and fluid-power systems.",
   "products": [
    {
     "id": "double_acting_pneumatic_cylinder",
     "name": "Double-Acting Pneumatic Cylinder",
     "description": "Pneumatic cylinder with double-acting operation.",
     "specs": [
      [
       "Product Type",
       "Pneumatic cylinder"
      ],
      [
       "General Use",
       "Linear motion"
      ],
      [
       "Action",
       "Double-acting"
      ]
     ]
    },
    {
     "id": "pneumatic_solenoid_directional_valve",
     "name": "Pneumatic Solenoid Directional Valve",
     "description": "Solenoid-operated valve for directing compressed air.",
     "specs": [
      [
       "Product Type",
       "Pneumatic valve"
      ],
      [
       "General Use",
       "Air flow control"
      ],
      [
       "Operation",
       "Solenoid"
      ]
     ]
    },
    {
     "id": "pneumatic_filter_regulator_lubricator_unit",
     "name": "Pneumatic Filter-Regulator-Lubricator Unit",
     "description": "Unit combining a filter, regulator and lubricator for compressed air.",
     "specs": [
      [
       "Product Type",
       "Air preparation unit"
      ],
      [
       "General Use",
       "Compressed-air conditioning"
      ]
     ]
    },
    {
     "id": "polyurethane_pneumatic_tubing",
     "name": "Polyurethane Pneumatic Tubing",
     "description": "Polyurethane tubing for compressed-air lines.",
     "specs": [
      [
       "Product Type",
       "Pneumatic tubing"
      ],
      [
       "General Use",
       "Air line connections"
      ],
      [
       "Material",
       "Polyurethane"
      ]
     ]
    },
    {
     "id": "pneumatic_push_in_fitting_set",
     "name": "Pneumatic Push-In Fitting Set",
     "description": "Set of push-in fittings for pneumatic tubing.",
     "specs": [
      [
       "Product Type",
       "Pneumatic fittings"
      ],
      [
       "General Use",
       "Tubing connections"
      ],
      [
       "Connection",
       "Push-in"
      ]
     ]
    },
    {
     "id": "hydraulic_cylinder",
     "name": "Hydraulic Cylinder",
     "description": "Cylinder for hydraulic systems.",
     "specs": [
      [
       "Product Type",
       "Hydraulic cylinder"
      ],
      [
       "General Use",
       "Linear motion"
      ]
     ]
    },
    {
     "id": "hydraulic_hose_assembly",
     "name": "Hydraulic Hose Assembly",
     "description": "Hose assembly for hydraulic lines.",
     "specs": [
      [
       "Product Type",
       "Hydraulic hose"
      ],
      [
       "General Use",
       "Hydraulic lines"
      ]
     ]
    },
    {
     "id": "hydraulic_quick_release_coupling",
     "name": "Hydraulic Quick-Release Coupling",
     "description": "Quick-release coupling for hydraulic lines.",
     "specs": [
      [
       "Product Type",
       "Hydraulic coupling"
      ],
      [
       "General Use",
       "Line connection"
      ],
      [
       "Type",
       "Quick-release"
      ]
     ]
    },
    {
     "id": "hydraulic_pressure_gauge",
     "name": "Hydraulic Pressure Gauge",
     "description": "Gauge for indicating hydraulic pressure.",
     "specs": [
      [
       "Product Type",
       "Pressure gauge"
      ],
      [
       "General Use",
       "Pressure indication"
      ]
     ]
    }
   ]
  },
  {
   "key": "bearings-couplings-power-transmission",
   "label": "Bearings, Couplings & Power Transmission",
   "icon": "fa-gears",
   "intro": "Bearings, couplings and transmission components for rotating machinery.",
   "products": [
    {
     "id": "deep_groove_ball_bearing",
     "name": "Deep-Groove Ball Bearing",
     "description": "Deep-groove ball bearing for rotating shafts.",
     "specs": [
      [
       "Product Type",
       "Ball bearing"
      ],
      [
       "General Use",
       "Shaft support"
      ],
      [
       "Type",
       "Deep-groove"
      ]
     ]
    },
    {
     "id": "tapered_roller_bearing",
     "name": "Tapered Roller Bearing",
     "description": "Tapered roller bearing for rotating shafts.",
     "specs": [
      [
       "Product Type",
       "Roller bearing"
      ],
      [
       "General Use",
       "Shaft support"
      ],
      [
       "Type",
       "Tapered roller"
      ]
     ]
    },
    {
     "id": "pillow_block_bearing_unit",
     "name": "Pillow Block Bearing Unit",
     "description": "Bearing unit in a pillow block housing.",
     "specs": [
      [
       "Product Type",
       "Bearing unit"
      ],
      [
       "General Use",
       "Shaft support"
      ],
      [
       "Housing",
       "Pillow block"
      ]
     ]
    },
    {
     "id": "jaw_coupling",
     "name": "Jaw Coupling",
     "description": "Jaw coupling for connecting shafts.",
     "specs": [
      [
       "Product Type",
       "Shaft coupling"
      ],
      [
       "General Use",
       "Shaft connection"
      ],
      [
       "Type",
       "Jaw"
      ]
     ]
    },
    {
     "id": "flexible_beam_coupling",
     "name": "Flexible Beam Coupling",
     "description": "Flexible beam coupling for connecting shafts.",
     "specs": [
      [
       "Product Type",
       "Shaft coupling"
      ],
      [
       "General Use",
       "Shaft connection"
      ],
      [
       "Type",
       "Flexible beam"
      ]
     ]
    },
    {
     "id": "industrial_v_belt",
     "name": "Industrial V-Belt",
     "description": "V-belt for power transmission.",
     "specs": [
      [
       "Product Type",
       "Drive belt"
      ],
      [
       "General Use",
       "Power transmission"
      ],
      [
       "Profile",
       "V"
      ]
     ]
    },
    {
     "id": "timing_belt",
     "name": "Timing Belt",
     "description": "Timing belt for synchronised drives.",
     "specs": [
      [
       "Product Type",
       "Drive belt"
      ],
      [
       "General Use",
       "Power transmission"
      ],
      [
       "Type",
       "Timing"
      ]
     ]
    },
    {
     "id": "roller_chain",
     "name": "Roller Chain",
     "description": "Roller chain for power transmission.",
     "specs": [
      [
       "Product Type",
       "Drive chain"
      ],
      [
       "General Use",
       "Power transmission"
      ],
      [
       "Type",
       "Roller"
      ]
     ]
    },
    {
     "id": "chain_sprocket",
     "name": "Chain Sprocket",
     "description": "Sprocket for use with chains.",
     "specs": [
      [
       "Product Type",
       "Sprocket"
      ],
      [
       "General Use",
       "Chain drives"
      ]
     ]
    }
   ]
  },
  {
   "key": "welding-equipment-consumables",
   "label": "Welding Equipment & Consumables",
   "icon": "fa-fire-flame-curved",
   "intro": "Welding equipment and consumables for fabrication and maintenance work.",
   "products": [
    {
     "id": "inverter_mma_welding_machine",
     "name": "Inverter MMA Welding Machine",
     "description": "Inverter-based MMA welding machine.",
     "specs": [
      [
       "Product Type",
       "Welding machine"
      ],
      [
       "General Use",
       "MMA welding"
      ],
      [
       "Process",
       "MMA"
      ]
     ]
    },
    {
     "id": "mig_mag_welding_machine",
     "name": "MIG/MAG Welding Machine",
     "description": "Welding machine for MIG/MAG welding.",
     "specs": [
      [
       "Product Type",
       "Welding machine"
      ],
      [
       "General Use",
       "MIG/MAG welding"
      ],
      [
       "Process",
       "MIG/MAG"
      ]
     ]
    },
    {
     "id": "tig_welding_machine",
     "name": "TIG Welding Machine",
     "description": "Welding machine for TIG welding.",
     "specs": [
      [
       "Product Type",
       "Welding machine"
      ],
      [
       "General Use",
       "TIG welding"
      ],
      [
       "Process",
       "TIG"
      ]
     ]
    },
    {
     "id": "mild_steel_welding_electrode",
     "name": "Mild Steel Welding Electrode",
     "description": "Welding electrode for mild steel.",
     "specs": [
      [
       "Product Type",
       "Welding electrode"
      ],
      [
       "General Use",
       "Welding"
      ],
      [
       "Base metal",
       "Mild steel"
      ]
     ]
    },
    {
     "id": "stainless_steel_welding_electrode",
     "name": "Stainless Steel Welding Electrode",
     "description": "Welding electrode for stainless steel.",
     "specs": [
      [
       "Product Type",
       "Welding electrode"
      ],
      [
       "General Use",
       "Welding"
      ],
      [
       "Base metal",
       "Stainless steel"
      ]
     ]
    },
    {
     "id": "mig_welding_wire_spool",
     "name": "MIG Welding Wire Spool",
     "description": "Welding wire on a spool for MIG welding.",
     "specs": [
      [
       "Product Type",
       "Welding wire"
      ],
      [
       "General Use",
       "MIG welding"
      ],
      [
       "Format",
       "Spool"
      ]
     ]
    },
    {
     "id": "tig_filler_rod",
     "name": "TIG Filler Rod",
     "description": "Filler rod for TIG welding.",
     "specs": [
      [
       "Product Type",
       "Filler rod"
      ],
      [
       "General Use",
       "TIG welding"
      ]
     ]
    },
    {
     "id": "welding_electrode_holder",
     "name": "Welding Electrode Holder",
     "description": "Holder for welding electrodes.",
     "specs": [
      [
       "Product Type",
       "Welding accessory"
      ],
      [
       "General Use",
       "Electrode holding"
      ]
     ]
    },
    {
     "id": "welding_earth_clamp",
     "name": "Welding Earth Clamp",
     "description": "Earth clamp for welding circuits.",
     "specs": [
      [
       "Product Type",
       "Welding accessory"
      ],
      [
       "General Use",
       "Earth connection"
      ]
     ]
    }
   ]
  },
  {
   "key": "industrial-cleaning-equipment-supplies",
   "label": "Industrial Cleaning Equipment & Supplies",
   "icon": "fa-broom",
   "intro": "Cleaning machines and supplies for factories, workshops and commercial facilities.",
   "products": [
    {
     "id": "wet_and_dry_industrial_vacuum_cleaner",
     "name": "Wet-and-Dry Industrial Vacuum Cleaner",
     "description": "Industrial vacuum cleaner for wet and dry use.",
     "specs": [
      [
       "Product Type",
       "Vacuum cleaner"
      ],
      [
       "General Use",
       "Cleaning"
      ],
      [
       "Use",
       "Wet and dry"
      ]
     ]
    },
    {
     "id": "high_pressure_washer",
     "name": "High-Pressure Washer",
     "description": "Washer for high-pressure cleaning.",
     "specs": [
      [
       "Product Type",
       "Pressure washer"
      ],
      [
       "General Use",
       "Washing"
      ]
     ]
    },
    {
     "id": "walk_behind_floor_scrubber",
     "name": "Walk-Behind Floor Scrubber",
     "description": "Walk-behind machine for scrubbing floors.",
     "specs": [
      [
       "Product Type",
       "Floor scrubber"
      ],
      [
       "General Use",
       "Floor cleaning"
      ],
      [
       "Operation",
       "Walk-behind"
      ]
     ]
    },
    {
     "id": "single_disc_floor_cleaning_machine",
     "name": "Single-Disc Floor Cleaning Machine",
     "description": "Floor cleaning machine with a single disc.",
     "specs": [
      [
       "Product Type",
       "Floor machine"
      ],
      [
       "General Use",
       "Floor cleaning"
      ],
      [
       "Disc",
       "Single"
      ]
     ]
    },
    {
     "id": "manual_floor_sweeper",
     "name": "Manual Floor Sweeper",
     "description": "Manual sweeper for floors.",
     "specs": [
      [
       "Product Type",
       "Sweeper"
      ],
      [
       "General Use",
       "Floor sweeping"
      ],
      [
       "Operation",
       "Manual"
      ]
     ]
    },
    {
     "id": "floor_squeegee",
     "name": "Floor Squeegee",
     "description": "Squeegee for clearing liquid from floors.",
     "specs": [
      [
       "Product Type",
       "Cleaning tool"
      ],
      [
       "General Use",
       "Floor cleaning"
      ]
     ]
    },
    {
     "id": "industrial_push_broom",
     "name": "Industrial Push Broom",
     "description": "Push broom for sweeping floors.",
     "specs": [
      [
       "Product Type",
       "Broom"
      ],
      [
       "General Use",
       "Floor sweeping"
      ]
     ]
    },
    {
     "id": "cotton_cleaning_waste",
     "name": "Cotton Cleaning Waste",
     "description": "Cotton waste for wiping and cleaning.",
     "specs": [
      [
       "Product Type",
       "Wiping material"
      ],
      [
       "General Use",
       "Wiping"
      ],
      [
       "Material",
       "Cotton"
      ]
     ]
    },
    {
     "id": "industrial_degreaser",
     "name": "Industrial Degreaser",
     "description": "Degreaser for cleaning oily and greasy surfaces.",
     "specs": [
      [
       "Product Type",
       "Cleaning chemical"
      ],
      [
       "General Use",
       "Degreasing"
      ]
     ]
    }
   ]
  },
  {
   "key": "power-backup-ups-voltage-stabilizers",
   "label": "Power Backup, UPS & Voltage Stabilizers",
   "icon": "fa-car-battery",
   "intro": "Backup power, UPS systems and voltage stabilizers for dependable electrical supply.",
   "products": [
    {
     "id": "line_interactive_ups",
     "name": "Line-Interactive UPS",
     "description": "Line-interactive UPS for backup power.",
     "specs": [
      [
       "Product Type",
       "UPS"
      ],
      [
       "General Use",
       "Backup power"
      ],
      [
       "Type",
       "Line-interactive"
      ]
     ]
    },
    {
     "id": "single_phase_online_ups",
     "name": "Single-Phase Online UPS",
     "description": "Single-phase online UPS for backup power.",
     "specs": [
      [
       "Product Type",
       "UPS"
      ],
      [
       "General Use",
       "Backup power"
      ],
      [
       "Type",
       "Online, single-phase"
      ]
     ]
    },
    {
     "id": "three_phase_online_ups",
     "name": "Three-Phase Online UPS",
     "description": "Three-phase online UPS for backup power.",
     "specs": [
      [
       "Product Type",
       "UPS"
      ],
      [
       "General Use",
       "Backup power"
      ],
      [
       "Type",
       "Online, three-phase"
      ]
     ]
    },
    {
     "id": "rack_mounted_online_ups",
     "name": "Rack-Mounted Online UPS",
     "description": "Online UPS for rack mounting.",
     "specs": [
      [
       "Product Type",
       "UPS"
      ],
      [
       "General Use",
       "Backup power"
      ],
      [
       "Mounting",
       "Rack"
      ]
     ]
    },
    {
     "id": "pure_sine_wave_inverter",
     "name": "Pure Sine Wave Inverter",
     "description": "Inverter with pure sine wave output.",
     "specs": [
      [
       "Product Type",
       "Inverter"
      ],
      [
       "General Use",
       "Power conversion"
      ],
      [
       "Output",
       "Pure sine wave"
      ]
     ]
    },
    {
     "id": "tubular_inverter_battery",
     "name": "Tubular Inverter Battery",
     "description": "Tubular battery for inverter use.",
     "specs": [
      [
       "Product Type",
       "Battery"
      ],
      [
       "General Use",
       "Inverter backup"
      ],
      [
       "Type",
       "Tubular"
      ]
     ]
    },
    {
     "id": "vrla_ups_battery",
     "name": "VRLA UPS Battery",
     "description": "VRLA battery for UPS use.",
     "specs": [
      [
       "Product Type",
       "Battery"
      ],
      [
       "General Use",
       "UPS backup"
      ],
      [
       "Type",
       "VRLA"
      ]
     ]
    },
    {
     "id": "single_phase_servo_voltage_stabilizer",
     "name": "Single-Phase Servo Voltage Stabilizer",
     "description": "Servo voltage stabilizer for single-phase supply.",
     "specs": [
      [
       "Product Type",
       "Voltage stabilizer"
      ],
      [
       "General Use",
       "Voltage stabilisation"
      ],
      [
       "Phase",
       "Single"
      ]
     ]
    },
    {
     "id": "three_phase_servo_voltage_stabilizer",
     "name": "Three-Phase Servo Voltage Stabilizer",
     "description": "Servo voltage stabilizer for three-phase supply.",
     "specs": [
      [
       "Product Type",
       "Voltage stabilizer"
      ],
      [
       "General Use",
       "Voltage stabilisation"
      ],
      [
       "Phase",
       "Three"
      ]
     ]
    }
   ]
  }
 ],
 "safety-packing": [
  {
   "key": "hand-body-protection",
   "label": "Hand & Body Protection",
   "icon": "fa-hand",
   "intro": "Gloves and body protection for workplace tasks.",
   "products": [
    {
     "id": "cotton_knitted_gloves",
     "name": "Cotton Knitted Gloves",
     "description": "Knitted cotton gloves for hand protection.",
     "specs": [
      [
       "Product Type",
       "Work gloves"
      ],
      [
       "General Use",
       "Hand protection"
      ],
      [
       "Material",
       "Cotton"
      ]
     ]
    },
    {
     "id": "pvc_dotted_handling_gloves",
     "name": "PVC-Dotted Handling Gloves",
     "description": "Gloves with PVC dots for handling.",
     "specs": [
      [
       "Product Type",
       "Work gloves"
      ],
      [
       "General Use",
       "Handling"
      ],
      [
       "Grip",
       "PVC dots"
      ]
     ]
    },
    {
     "id": "pu_coated_work_gloves",
     "name": "PU-Coated Work Gloves",
     "description": "Work gloves with a PU coating.",
     "specs": [
      [
       "Product Type",
       "Work gloves"
      ],
      [
       "General Use",
       "Hand protection"
      ],
      [
       "Coating",
       "PU"
      ]
     ]
    },
    {
     "id": "nitrile_coated_work_gloves",
     "name": "Nitrile-Coated Work Gloves",
     "description": "Work gloves with a nitrile coating.",
     "specs": [
      [
       "Product Type",
       "Work gloves"
      ],
      [
       "General Use",
       "Hand protection"
      ],
      [
       "Coating",
       "Nitrile"
      ]
     ]
    },
    {
     "id": "leather_welding_gloves",
     "name": "Leather Welding Gloves",
     "description": "Leather gloves for welding work.",
     "specs": [
      [
       "Product Type",
       "Welding gloves"
      ],
      [
       "General Use",
       "Welding"
      ],
      [
       "Material",
       "Leather"
      ]
     ]
    },
    {
     "id": "chemical_resistant_gauntlet_gloves",
     "name": "Chemical-Resistant Gauntlet Gloves",
     "description": "Gauntlet gloves for chemical-handling tasks.",
     "specs": [
      [
       "Product Type",
       "Gauntlet gloves"
      ],
      [
       "General Use",
       "Chemical handling"
      ],
      [
       "Style",
       "Gauntlet"
      ]
     ]
    },
    {
     "id": "cut_resistant_work_gloves",
     "name": "Cut-Resistant Work Gloves",
     "description": "Work gloves described as cut-resistant.",
     "specs": [
      [
       "Product Type",
       "Work gloves"
      ],
      [
       "General Use",
       "Handling"
      ]
     ]
    },
    {
     "id": "reflective_safety_vest",
     "name": "Reflective Safety Vest",
     "description": "Vest with reflective elements for visibility.",
     "specs": [
      [
       "Product Type",
       "High-visibility vest"
      ],
      [
       "General Use",
       "Visibility"
      ]
     ]
    },
    {
     "id": "industrial_work_coverall",
     "name": "Industrial Work Coverall",
     "description": "Coverall for industrial work.",
     "specs": [
      [
       "Product Type",
       "Coverall"
      ],
      [
       "General Use",
       "Body protection"
      ]
     ]
    }
   ]
  },
  {
   "key": "safety-footwear-head-protection",
   "label": "Safety Footwear & Head Protection",
   "icon": "fa-helmet-safety",
   "intro": "Protective footwear and head protection for industrial and commercial workplaces.",
   "products": [
    {
     "id": "lace_up_safety_shoe",
     "name": "Lace-Up Safety Shoe",
     "description": "Safety shoe with lace-up closure.",
     "specs": [
      [
       "Product Type",
       "Safety shoe"
      ],
      [
       "General Use",
       "Foot protection"
      ],
      [
       "Closure",
       "Lace-up"
      ]
     ]
    },
    {
     "id": "slip_on_safety_shoe",
     "name": "Slip-On Safety Shoe",
     "description": "Safety shoe with slip-on closure.",
     "specs": [
      [
       "Product Type",
       "Safety shoe"
      ],
      [
       "General Use",
       "Foot protection"
      ],
      [
       "Closure",
       "Slip-on"
      ]
     ]
    },
    {
     "id": "high_ankle_safety_boot",
     "name": "High-Ankle Safety Boot",
     "description": "Safety boot with a high ankle.",
     "specs": [
      [
       "Product Type",
       "Safety boot"
      ],
      [
       "General Use",
       "Foot protection"
      ],
      [
       "Height",
       "High-ankle"
      ]
     ]
    },
    {
     "id": "pvc_safety_gumboot",
     "name": "PVC Safety Gumboot",
     "description": "PVC gumboot for work use.",
     "specs": [
      [
       "Product Type",
       "Gumboot"
      ],
      [
       "General Use",
       "Foot protection"
      ],
      [
       "Material",
       "PVC"
      ]
     ]
    },
    {
     "id": "esd_safety_shoe",
     "name": "ESD Safety Shoe",
     "description": "Safety shoe for ESD-controlled areas.",
     "specs": [
      [
       "Product Type",
       "Safety shoe"
      ],
      [
       "General Use",
       "ESD-controlled areas"
      ],
      [
       "Type",
       "ESD"
      ]
     ]
    },
    {
     "id": "standard_industrial_safety_helmet",
     "name": "Standard Industrial Safety Helmet",
     "description": "Safety helmet for head protection.",
     "specs": [
      [
       "Product Type",
       "Safety helmet"
      ],
      [
       "General Use",
       "Head protection"
      ],
      [
       "Type",
       "Standard"
      ]
     ]
    },
    {
     "id": "vented_industrial_safety_helmet",
     "name": "Vented Industrial Safety Helmet",
     "description": "Safety helmet with vents.",
     "specs": [
      [
       "Product Type",
       "Safety helmet"
      ],
      [
       "General Use",
       "Head protection"
      ],
      [
       "Type",
       "Vented"
      ]
     ]
    },
    {
     "id": "industrial_bump_cap",
     "name": "Industrial Bump Cap",
     "description": "Bump cap for minor head bumps.",
     "specs": [
      [
       "Product Type",
       "Bump cap"
      ],
      [
       "General Use",
       "Head protection"
      ]
     ]
    },
    {
     "id": "helmet_chin_strap",
     "name": "Helmet Chin Strap",
     "description": "Chin strap for securing a safety helmet.",
     "specs": [
      [
       "Product Type",
       "Helmet accessory"
      ],
      [
       "General Use",
       "Helmet securing"
      ]
     ]
    }
   ]
  },
  {
   "key": "eye-face-hearing-respiratory-protection",
   "label": "Eye, Face, Hearing & Respiratory Protection",
   "icon": "fa-glasses",
   "intro": "Protection for eyes, face, hearing and breathing at work.",
   "products": [
    {
     "id": "clear_safety_spectacles",
     "name": "Clear Safety Spectacles",
     "description": "Clear safety spectacles for eye protection.",
     "specs": [
      [
       "Product Type",
       "Safety spectacles"
      ],
      [
       "General Use",
       "Eye protection"
      ],
      [
       "Lens",
       "Clear"
      ]
     ]
    },
    {
     "id": "chemical_splash_goggles",
     "name": "Chemical Splash Goggles",
     "description": "Goggles for eye protection when handling liquids.",
     "specs": [
      [
       "Product Type",
       "Safety goggles"
      ],
      [
       "General Use",
       "Eye protection"
      ]
     ]
    },
    {
     "id": "clear_face_shield",
     "name": "Clear Face Shield",
     "description": "Clear face shield for face protection.",
     "specs": [
      [
       "Product Type",
       "Face shield"
      ],
      [
       "General Use",
       "Face protection"
      ],
      [
       "Visor",
       "Clear"
      ]
     ]
    },
    {
     "id": "welding_helmet",
     "name": "Welding Helmet",
     "description": "Welding helmet for face and eye protection while welding.",
     "specs": [
      [
       "Product Type",
       "Welding helmet"
      ],
      [
       "General Use",
       "Welding"
      ]
     ]
    },
    {
     "id": "disposable_foam_earplugs",
     "name": "Disposable Foam Earplugs",
     "description": "Disposable foam earplugs for hearing protection.",
     "specs": [
      [
       "Product Type",
       "Earplugs"
      ],
      [
       "General Use",
       "Hearing protection"
      ],
      [
       "Format",
       "Disposable foam"
      ]
     ]
    },
    {
     "id": "reusable_earplugs",
     "name": "Reusable Earplugs",
     "description": "Reusable earplugs for hearing protection.",
     "specs": [
      [
       "Product Type",
       "Earplugs"
      ],
      [
       "General Use",
       "Hearing protection"
      ],
      [
       "Format",
       "Reusable"
      ]
     ]
    },
    {
     "id": "ear_defenders",
     "name": "Ear Defenders",
     "description": "Ear defenders for hearing protection.",
     "specs": [
      [
       "Product Type",
       "Ear defenders"
      ],
      [
       "General Use",
       "Hearing protection"
      ]
     ]
    },
    {
     "id": "disposable_particulate_respirator",
     "name": "Disposable Particulate Respirator",
     "description": "Disposable respirator for particulate filtering.",
     "specs": [
      [
       "Product Type",
       "Respirator"
      ],
      [
       "General Use",
       "Respiratory protection"
      ],
      [
       "Format",
       "Disposable"
      ]
     ]
    },
    {
     "id": "reusable_half_face_respirator",
     "name": "Reusable Half-Face Respirator",
     "description": "Reusable half-face respirator.",
     "specs": [
      [
       "Product Type",
       "Respirator"
      ],
      [
       "General Use",
       "Respiratory protection"
      ],
      [
       "Format",
       "Reusable half-face"
      ]
     ]
    }
   ]
  },
  {
   "key": "workplace-safety-signage-fire-safety",
   "label": "Workplace Safety, Signage & Fire Safety",
   "icon": "fa-triangle-exclamation",
   "intro": "Safety signage, barriers and fire safety supplies for workplaces.",
   "products": [
    {
     "id": "traffic_safety_cone",
     "name": "Traffic Safety Cone",
     "description": "Cone for marking traffic and work zones.",
     "specs": [
      [
       "Product Type",
       "Safety cone"
      ],
      [
       "General Use",
       "Area marking"
      ]
     ]
    },
    {
     "id": "folding_floor_caution_sign",
     "name": "Folding Floor Caution Sign",
     "description": "Folding caution sign for floor areas.",
     "specs": [
      [
       "Product Type",
       "Caution sign"
      ],
      [
       "General Use",
       "Hazard warning"
      ],
      [
       "Design",
       "Folding"
      ]
     ]
    },
    {
     "id": "reflective_safety_bollard",
     "name": "Reflective Safety Bollard",
     "description": "Bollard with reflective surfaces for marking areas.",
     "specs": [
      [
       "Product Type",
       "Safety bollard"
      ],
      [
       "General Use",
       "Area marking"
      ],
      [
       "Surface",
       "Reflective"
      ]
     ]
    },
    {
     "id": "retractable_belt_barrier",
     "name": "Retractable Belt Barrier",
     "description": "Barrier with a retractable belt for guiding and restricting areas.",
     "specs": [
      [
       "Product Type",
       "Belt barrier"
      ],
      [
       "General Use",
       "Area control"
      ],
      [
       "Belt",
       "Retractable"
      ]
     ]
    },
    {
     "id": "safety_sign_board",
     "name": "Safety Sign Board",
     "description": "Sign board for safety messages.",
     "specs": [
      [
       "Product Type",
       "Safety sign"
      ],
      [
       "General Use",
       "Safety messaging"
      ]
     ]
    },
    {
     "id": "lockout_tagout_kit",
     "name": "Lockout/Tagout Kit",
     "description": "Kit for lockout/tagout procedures.",
     "specs": [
      [
       "Product Type",
       "Isolation kit"
      ],
      [
       "General Use",
       "Equipment isolation"
      ]
     ]
    },
    {
     "id": "abc_dry_powder_fire_extinguisher",
     "name": "ABC Dry Powder Fire Extinguisher",
     "description": "Portable fire extinguisher with ABC dry powder.",
     "specs": [
      [
       "Product Type",
       "Fire extinguisher"
      ],
      [
       "General Use",
       "Fire response"
      ],
      [
       "Agent",
       "ABC dry powder"
      ]
     ]
    },
    {
     "id": "co2_fire_extinguisher",
     "name": "CO₂ Fire Extinguisher",
     "description": "Portable fire extinguisher using CO₂.",
     "specs": [
      [
       "Product Type",
       "Fire extinguisher"
      ],
      [
       "General Use",
       "Fire response"
      ],
      [
       "Agent",
       "CO₂"
      ]
     ]
    },
    {
     "id": "fire_blanket",
     "name": "Fire Blanket",
     "description": "Blanket for fire response.",
     "specs": [
      [
       "Product Type",
       "Fire blanket"
      ],
      [
       "General Use",
       "Fire response"
      ]
     ]
    }
   ]
  },
  {
   "key": "packing-tapes-adhesives-sealants",
   "label": "Packing Tapes, Adhesives & Sealants",
   "icon": "fa-tape",
   "intro": "Tapes, adhesives and sealants for packing, sealing and bonding.",
   "products": [
    {
     "id": "bopp_carton_sealing_tape",
     "name": "BOPP Carton Sealing Tape",
     "description": "BOPP tape for sealing cartons.",
     "specs": [
      [
       "Product Type",
       "Packing tape"
      ],
      [
       "General Use",
       "Carton sealing"
      ],
      [
       "Material",
       "BOPP"
      ]
     ]
    },
    {
     "id": "printed_fragile_packing_tape",
     "name": "Printed Fragile Packing Tape",
     "description": "Packing tape printed with a fragile message.",
     "specs": [
      [
       "Product Type",
       "Packing tape"
      ],
      [
       "General Use",
       "Carton sealing"
      ],
      [
       "Print",
       "Fragile"
      ]
     ]
    },
    {
     "id": "masking_tape",
     "name": "Masking Tape",
     "description": "Masking tape for masking and temporary holding.",
     "specs": [
      [
       "Product Type",
       "Masking tape"
      ],
      [
       "General Use",
       "Masking"
      ]
     ]
    },
    {
     "id": "double_sided_foam_tape",
     "name": "Double-Sided Foam Tape",
     "description": "Foam tape with adhesive on both sides.",
     "specs": [
      [
       "Product Type",
       "Foam tape"
      ],
      [
       "General Use",
       "Mounting and bonding"
      ],
      [
       "Sides",
       "Double-sided"
      ]
     ]
    },
    {
     "id": "reinforced_filament_tape",
     "name": "Reinforced Filament Tape",
     "description": "Reinforced filament tape for packing.",
     "specs": [
      [
       "Product Type",
       "Filament tape"
      ],
      [
       "General Use",
       "Packing"
      ],
      [
       "Construction",
       "Reinforced"
      ]
     ]
    },
    {
     "id": "cloth_duct_tape",
     "name": "Cloth Duct Tape",
     "description": "Cloth duct tape for general taping.",
     "specs": [
      [
       "Product Type",
       "Duct tape"
      ],
      [
       "General Use",
       "General taping"
      ],
      [
       "Backing",
       "Cloth"
      ]
     ]
    },
    {
     "id": "hot_melt_glue_stick",
     "name": "Hot-Melt Glue Stick",
     "description": "Glue stick for hot-melt glue guns.",
     "specs": [
      [
       "Product Type",
       "Glue stick"
      ],
      [
       "General Use",
       "Bonding"
      ],
      [
       "Type",
       "Hot-melt"
      ]
     ]
    },
    {
     "id": "silicone_sealant_cartridge",
     "name": "Silicone Sealant Cartridge",
     "description": "Silicone sealant supplied in a cartridge.",
     "specs": [
      [
       "Product Type",
       "Sealant"
      ],
      [
       "General Use",
       "Sealing"
      ],
      [
       "Format",
       "Cartridge"
      ]
     ]
    },
    {
     "id": "two_part_epoxy_adhesive",
     "name": "Two-Part Epoxy Adhesive",
     "description": "Two-part epoxy adhesive for bonding.",
     "specs": [
      [
       "Product Type",
       "Adhesive"
      ],
      [
       "General Use",
       "Bonding"
      ],
      [
       "Type",
       "Two-part epoxy"
      ]
     ]
    }
   ]
  },
  {
   "key": "stretch-film-bubble-wrap-cushioning",
   "label": "Stretch Film, Bubble Wrap & Cushioning",
   "icon": "fa-box-open",
   "intro": "Stretch film, bubble wrap and cushioning materials for protecting goods in storage and transit.",
   "products": [
    {
     "id": "manual_stretch_film_roll",
     "name": "Manual Stretch Film Roll",
     "description": "Stretch film roll for manual wrapping.",
     "specs": [
      [
       "Product Type",
       "Stretch film"
      ],
      [
       "General Use",
       "Load wrapping"
      ],
      [
       "Application",
       "Manual"
      ]
     ]
    },
    {
     "id": "machine_stretch_film_roll",
     "name": "Machine Stretch Film Roll",
     "description": "Stretch film roll for machine wrapping.",
     "specs": [
      [
       "Product Type",
       "Stretch film"
      ],
      [
       "General Use",
       "Load wrapping"
      ],
      [
       "Application",
       "Machine"
      ]
     ]
    },
    {
     "id": "mini_stretch_film_roll",
     "name": "Mini Stretch Film Roll",
     "description": "Mini stretch film roll for wrapping.",
     "specs": [
      [
       "Product Type",
       "Stretch film"
      ],
      [
       "General Use",
       "Wrapping"
      ],
      [
       "Format",
       "Mini roll"
      ]
     ]
    },
    {
     "id": "air_bubble_wrap_roll",
     "name": "Air Bubble Wrap Roll",
     "description": "Bubble wrap roll for cushioning during packing.",
     "specs": [
      [
       "Product Type",
       "Bubble wrap"
      ],
      [
       "General Use",
       "Cushioning"
      ],
      [
       "Format",
       "Roll"
      ]
     ]
    },
    {
     "id": "epe_foam_roll",
     "name": "EPE Foam Roll",
     "description": "EPE foam roll for cushioning.",
     "specs": [
      [
       "Product Type",
       "Foam roll"
      ],
      [
       "General Use",
       "Cushioning"
      ],
      [
       "Material",
       "EPE foam"
      ]
     ]
    },
    {
     "id": "epe_foam_sheet",
     "name": "EPE Foam Sheet",
     "description": "EPE foam sheet for cushioning.",
     "specs": [
      [
       "Product Type",
       "Foam sheet"
      ],
      [
       "General Use",
       "Cushioning"
      ],
      [
       "Material",
       "EPE foam"
      ]
     ]
    },
    {
     "id": "corrugated_cushioning_roll",
     "name": "Corrugated Cushioning Roll",
     "description": "Corrugated roll for cushioning and wrapping.",
     "specs": [
      [
       "Product Type",
       "Cushioning roll"
      ],
      [
       "General Use",
       "Cushioning"
      ],
      [
       "Format",
       "Roll"
      ]
     ]
    },
    {
     "id": "air_cushion_film_roll",
     "name": "Air Cushion Film Roll",
     "description": "Film roll for air cushion packaging.",
     "specs": [
      [
       "Product Type",
       "Air cushion film"
      ],
      [
       "General Use",
       "Cushioning"
      ],
      [
       "Format",
       "Roll"
      ]
     ]
    },
    {
     "id": "foam_edge_protector",
     "name": "Foam Edge Protector",
     "description": "Foam protector for edges during packing.",
     "specs": [
      [
       "Product Type",
       "Edge protector"
      ],
      [
       "General Use",
       "Edge protection"
      ],
      [
       "Material",
       "Foam"
      ]
     ]
    }
   ]
  },
  {
   "key": "cartons-strapping-packing-accessories",
   "label": "Cartons, Strapping & Packing Accessories",
   "icon": "fa-boxes-stacked",
   "intro": "Cartons, strapping and accessories for packing and bundling goods.",
   "products": [
    {
     "id": "three_ply_corrugated_carton",
     "name": "Three-Ply Corrugated Carton",
     "description": "Corrugated carton with three plies.",
     "specs": [
      [
       "Product Type",
       "Carton"
      ],
      [
       "General Use",
       "Packing"
      ],
      [
       "Plies",
       "Three"
      ]
     ]
    },
    {
     "id": "five_ply_corrugated_carton",
     "name": "Five-Ply Corrugated Carton",
     "description": "Corrugated carton with five plies.",
     "specs": [
      [
       "Product Type",
       "Carton"
      ],
      [
       "General Use",
       "Packing"
      ],
      [
       "Plies",
       "Five"
      ]
     ]
    },
    {
     "id": "seven_ply_corrugated_carton",
     "name": "Seven-Ply Corrugated Carton",
     "description": "Corrugated carton with seven plies.",
     "specs": [
      [
       "Product Type",
       "Carton"
      ],
      [
       "General Use",
       "Packing"
      ],
      [
       "Plies",
       "Seven"
      ]
     ]
    },
    {
     "id": "pp_strapping_roll",
     "name": "PP Strapping Roll",
     "description": "PP strapping roll for bundling and packing.",
     "specs": [
      [
       "Product Type",
       "Strapping"
      ],
      [
       "General Use",
       "Bundling"
      ],
      [
       "Material",
       "PP"
      ]
     ]
    },
    {
     "id": "pet_strapping_roll",
     "name": "PET Strapping Roll",
     "description": "PET strapping roll for bundling and packing.",
     "specs": [
      [
       "Product Type",
       "Strapping"
      ],
      [
       "General Use",
       "Bundling"
      ],
      [
       "Material",
       "PET"
      ]
     ]
    },
    {
     "id": "steel_strapping_coil",
     "name": "Steel Strapping Coil",
     "description": "Steel strapping coil for bundling and packing.",
     "specs": [
      [
       "Product Type",
       "Strapping"
      ],
      [
       "General Use",
       "Bundling"
      ],
      [
       "Material",
       "Steel"
      ]
     ]
    },
    {
     "id": "strapping_seal_buckle_set",
     "name": "Strapping Seal & Buckle Set",
     "description": "Seals and buckles for strapping.",
     "specs": [
      [
       "Product Type",
       "Strapping accessory"
      ],
      [
       "General Use",
       "Strap fastening"
      ]
     ]
    },
    {
     "id": "manual_strapping_tool_set",
     "name": "Manual Strapping Tool Set",
     "description": "Manual tool set for strapping.",
     "specs": [
      [
       "Product Type",
       "Strapping tool"
      ],
      [
       "General Use",
       "Strapping"
      ],
      [
       "Operation",
       "Manual"
      ]
     ]
    },
    {
     "id": "handheld_carton_tape_dispenser",
     "name": "Handheld Carton Tape Dispenser",
     "description": "Handheld dispenser for carton tape.",
     "specs": [
      [
       "Product Type",
       "Tape dispenser"
      ],
      [
       "General Use",
       "Tape dispensing"
      ],
      [
       "Operation",
       "Handheld"
      ]
     ]
    }
   ]
  }
 ]
}
