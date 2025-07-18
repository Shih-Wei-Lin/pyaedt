Cutout
======

The **Layout cutout** extension allows users to create cutouts in HFSS 3D Layout designs based on selected nets.

The extension provides a graphical user interface (GUI) for configuration,
or it can be used in batch mode via command line arguments.

The following image shows the extension user interface:

.. image:: ../../../_static/extensions/cutout_ui.png
  :width: 800
  :alt: Parametrize Layout


Features
--------

- Customizable options for fixing disjoint nets, selecting the cutout type, and applying expansion factors.
- Integration with Ansys EDB for layout cutout creation and post-processing.
- Switch between light and dark themes in the GUI.


Using the extension
-------------------

1. Open the **Automation** tab in the HFSS 3D Layout interface.
2. Locate and click the **Layout Cutout** icon under the Extension Manager.
3. In the GUI, users can interact with the following elements:
   - **Cutout type**: A dropdown menu to select the desired cutout type (ConvexHull, Bounding, Conforming).
   - **Expansion factor**: A text box to define the expansion factor for the cutout (in mm).
   - **Fix disjoint nets**: A checkbox to enable or disable fixing of disjoint nets.
   - **Select signal nets in layout**: A button to select signal nets from the layout.
   - **Select reference nets**: A button to select reference nets.
   - **Reset selection**: A button to clear the current selections of signal and reference nets.
   - **Theme toggle**: A button to switch between light and dark modes for the GUI.
4. Click on **Create Cutout** to generate the cutout.


Command line
------------

The extension can also be used directly via the command line for batch processing.

Supported arguments include:

- `cutout_type`: Type of cutout to apply (default value is "ConvexHull").
- `signals`: List of signal nets to use for the cutout.
- `references`: List of reference nets to use for the cutout.
- `expansion_factor`: Expansion factor in "mm" for the cutout.
- `fix_disjoints`: Boolean flag to enable or disable fixing of disjoint nets.

Use the following syntax to run the extension:

.. toctree::
   :maxdepth: 2

   ../commandline
