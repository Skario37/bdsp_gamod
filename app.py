from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QCheckBox, QButtonGroup, QRadioButton, QLabel, QSpinBox, QTextEdit, QPushButton, QFileDialog
from PySide2.QtGui import QPalette, QColor, Qt, QPixmap
from PySide2.QtCore import QSize
from os import path
from Gamod import Main
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initValues()

        # set the title
        self.setWindowTitle("BDSP Gamod")
        # setting  the geometry of window
        self.setGeometry(0, 0, 480, 360)
        
        ## set options layout
        # self.setCentralWidget(QPushButton("options"))
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)


        # Set Main Layout
        self.mLayout = QHBoxLayout(self.centralWidget)
        self.mLayout.setObjectName(u"mLayout")
        self.setLayout(self.mLayout)

        # Set Options Layout
        self.oWidget = QWidget(self.centralWidget)
        self.oWidget.setObjectName(u"oWidget")
        self.mLayout.addWidget(self.oWidget)
        self.oLayout = QVBoxLayout(self.oWidget)
        self.oLayout.setObjectName(u"oLayout")
        self.oLayout.setAlignment(Qt.AlignTop)
        self.oWidget.setLayout(self.oLayout)

        # Set Utils Layout
        self.uWidget = QWidget(self.centralWidget)
        self.uWidget.setObjectName(u"uWidget")
        self.mLayout.addWidget(self.uWidget)
        self.uLayout = QVBoxLayout(self.uWidget)
        self.uLayout.setObjectName(u"uLayout")
        self.uLayout.setAlignment(Qt.AlignTop)
        self.uWidget.setLayout(self.uLayout)

        # Set Console Layout
        self.cWidget = QWidget(self.centralWidget)
        self.cWidget.setObjectName(u"cWidget")
        self.mLayout.addWidget(self.cWidget)
        self.cLayout = QVBoxLayout(self.cWidget)
        self.cLayout.setObjectName(u"cLayout")
        self.cWidget.setLayout(self.cLayout)

        # Set Options
        ## Select generations
        self.monOpts = QGroupBox(self.oWidget)
        self.monOpts.setObjectName(u"monOpts")
        self.monOpts.setTitle(u"Pokémon Options")
        self.oLayout.addWidget(self.monOpts)
        self.monOptsLayout = QHBoxLayout(self.monOpts)
        self.monOptsLayout.setObjectName(u"monOptsLayout")
        self.monOpts.setLayout(self.monOptsLayout)
        ### Gen1
        self.cbGen1 = QCheckBox(self.monOpts)
        self.cbGen1.setObjectName(u"cbGen1")
        self.cbGen1.setText(u"Gen 1")
        self.cbGen1.setChecked(True)
        self.monOptsLayout.addWidget(self.cbGen1)
        ### Gen2
        self.cbGen2 = QCheckBox(self.monOpts)
        self.cbGen2.setObjectName(u"cbGen2")
        self.cbGen2.setText(u"Gen 2")
        self.cbGen2.setChecked(True)
        self.monOptsLayout.addWidget(self.cbGen2)
        ### Gen3
        self.cbGen3 = QCheckBox(self.monOpts)
        self.cbGen3.setObjectName(u"cbGen3")
        self.cbGen3.setText(u"Gen 3")
        self.cbGen3.setChecked(True)
        self.monOptsLayout.addWidget(self.cbGen3)
        ### Gen4
        self.cbGen4 = QCheckBox(self.monOpts)
        self.cbGen4.setObjectName(u"cbGen4")
        self.cbGen4.setText(u"Gen 4")
        self.cbGen4.setChecked(True)
        self.monOptsLayout.addWidget(self.cbGen4)
        ### Leg
        self.cbLeg = QCheckBox(self.monOpts)
        self.cbLeg.setObjectName(u"cbLeg")
        self.cbLeg.setText(u"Keep legendaries as legendaries")
        self.cbLeg.setChecked(True)
        self.monOptsLayout.addWidget(self.cbLeg)

        ## Randomizers
        self.groupRnd = QGroupBox(self.oWidget)
        self.groupRnd.setObjectName(u"groupRnd")
        self.groupRnd.setTitle(u"Randomizer Options")
        self.oLayout.addWidget(self.groupRnd)
        self.groupRndLayout = QVBoxLayout(self.groupRnd)
        self.groupRndLayout.setObjectName(u"groupRndLayout")
        self.groupRnd.setLayout(self.groupRndLayout)
        ### Starters
        self.cbStarters = QCheckBox(self.groupRnd)
        self.cbStarters.setObjectName(u"cbStarters")
        self.cbStarters.setText(u"Starters")
        self.groupRndLayout.addWidget(self.cbStarters)
        ### Evolutions
        self.cbEvolutions = QCheckBox(self.groupRnd)
        self.cbEvolutions.setObjectName(u"cbEvolutions")
        self.cbEvolutions.setText(u"Evolutions")
        self.groupRndLayout.addWidget(self.cbEvolutions)
        ### Types
        self.cbTypes = QCheckBox(self.groupRnd)
        self.cbTypes.setObjectName(u"cbTypes")
        self.cbTypes.setText(u"Types")
        self.groupRndLayout.addWidget(self.cbTypes)
        ### Egg Moves
        self.cbEggMoves = QCheckBox(self.groupRnd)
        self.cbEggMoves.setObjectName(u"cbEggMoves")
        self.cbEggMoves.setText(u"Egg Moves")
        self.groupRndLayout.addWidget(self.cbEggMoves)
        ### Egg Groups
        self.cbEggGroups = QCheckBox(self.groupRnd)
        self.cbEggGroups.setObjectName(u"cbEggGroups")
        self.cbEggGroups.setText(u"Egg Groups")
        self.groupRndLayout.addWidget(self.cbEggGroups)

        ### Encounters
        self.groupEnc = QGroupBox(self.oWidget)
        self.groupEnc.setObjectName(u"groupEnc")
        self.groupEnc.setTitle(u"Encounters")
        self.groupRndLayout.addWidget(self.groupEnc)
        self.groupEncLayout = QHBoxLayout(self.groupEnc)
        self.groupEncLayout.setObjectName(u"groupEncLayout")
        self.groupEnc.setLayout(self.groupEncLayout)
        #### Field
        self.cbEncField = QCheckBox(self.groupEnc)
        self.cbEncField.setObjectName(u"cbEncField")
        self.cbEncField.setText(u"Field")
        self.groupEncLayout.addWidget(self.cbEncField)
        #### Safari
        self.cbEncSafari = QCheckBox(self.groupEnc)
        self.cbEncSafari.setObjectName(u"cbEncSafari")
        self.cbEncSafari.setText(u"Safari")
        self.groupEncLayout.addWidget(self.cbEncSafari)
        #### Underground
        self.cbEncUg = QCheckBox(self.groupEnc)
        self.cbEncUg.setObjectName(u"cbEncUg")
        self.cbEncUg.setText(u"Underground")
        self.groupEncLayout.addWidget(self.cbEncUg)
        ### Trainers
        self.groupTrainers = QGroupBox(self.oWidget)
        self.groupTrainers.setObjectName(u"groupTrainers")
        self.groupTrainers.setTitle(u"Trainers")
        self.groupRndLayout.addWidget(self.groupTrainers)
        self.groupTrainersLayout = QVBoxLayout(self.groupTrainers)
        self.groupTrainersLayout.setObjectName(u"groupTrainersLayout")
        self.groupTrainers.setLayout(self.groupTrainersLayout)
        #### Items
        self.cbTrainersItems = QCheckBox(self.groupTrainers)
        self.cbTrainersItems.setObjectName(u"cbTrainersItems")
        self.cbTrainersItems.setText(u"Items used by trainers")
        self.groupTrainersLayout.addWidget(self.cbTrainersItems)
        #### Trainers Monster
        self.groupTrainersMons = QGroupBox(self.groupTrainers)
        self.groupTrainersMons.setObjectName(u"groupTrainersMons")
        self.groupTrainersMons.setTitle(u"Pokémon")
        self.groupTrainersLayout.addWidget(self.groupTrainersMons)
        self.groupTrainersMonsLayout = QHBoxLayout(self.groupTrainersMons)
        self.groupTrainersMonsLayout.setObjectName(u"groupTrainersMonsLayout")
        self.groupTrainersMons.setLayout(self.groupTrainersMonsLayout)
        ##### Field Trainers
        self.cbTrainersField = QCheckBox(self.groupTrainersMons)
        self.cbTrainersField.setObjectName(u"cbTrainersField")
        self.cbTrainersField.setText(u"Field trainers")
        self.groupTrainersMonsLayout.addWidget(self.cbTrainersField)
        ##### Tower Trainers
        self.cbTrainersTower = QCheckBox(self.groupTrainersMons)
        self.cbTrainersTower.setObjectName(u"cbTrainersTower")
        self.cbTrainersTower.setText(u"Tower trainers")
        self.groupTrainersMonsLayout.addWidget(self.cbTrainersTower)
        #### IV's
        self.groupIV = QGroupBox(self.groupTrainers)
        self.groupIV.setObjectName(u"groupIV")
        self.groupIV.setTitle(u"IV's")
        self.groupTrainersLayout.addWidget(self.groupIV)
        self.groupIVLayout = QHBoxLayout(self.groupIV)
        self.groupIVLayout.setObjectName(u"groupIVLayout")
        self.groupIV.setLayout(self.groupIVLayout)
        ##### IV's default & randomize & maximize
        self.radioGroupIV = QButtonGroup(self.groupIV)
        self.rbDefaultIV = QRadioButton("IV")
        self.rbDefaultIV.setObjectName(u"rbDefaultIV")
        self.rbDefaultIV.setText(u"Default")
        self.rbDefaultIV.setChecked(True)
        self.rbRandomizeIV = QRadioButton("IV")
        self.rbRandomizeIV.setObjectName(u"rbRandomizeIV")
        self.rbRandomizeIV.setText(u"Randomize")
        self.rbMaximizeIV = QRadioButton("IV")
        self.rbMaximizeIV.setObjectName(u"rbMaximizeIV")
        self.rbMaximizeIV.setText(u"Maximize")
        self.radioGroupIV.addButton(self.rbDefaultIV)
        self.radioGroupIV.addButton(self.rbRandomizeIV)
        self.radioGroupIV.addButton(self.rbMaximizeIV)
        self.groupIVLayout.addWidget(self.rbDefaultIV)
        self.groupIVLayout.addWidget(self.rbRandomizeIV)
        self.groupIVLayout.addWidget(self.rbMaximizeIV)
        #### EV's
        self.groupEV = QGroupBox(self.groupTrainers)
        self.groupEV.setObjectName(u"groupEV")
        self.groupEV.setTitle(u"EV's")
        self.groupTrainersLayout.addWidget(self.groupEV)
        self.groupEVLayout = QHBoxLayout(self.groupEV)
        self.groupEVLayout.setObjectName(u"groupEVLayout")
        self.groupEV.setLayout(self.groupEVLayout)
        ##### EV's default & randomize & maximize
        self.radioGroupEV = QButtonGroup(self.groupEV)
        self.rbDefaultEV = QRadioButton("EV")
        self.rbDefaultEV.setObjectName(u"rbDefaultEV")
        self.rbDefaultEV.setText(u"Default")
        self.rbDefaultEV.setChecked(True)
        self.rbRandomizeEV = QRadioButton("EV")
        self.rbRandomizeEV.setObjectName(u"rbRandomizeEV")
        self.rbRandomizeEV.setText(u"Randomize")
        self.rbMaximizeEV = QRadioButton("EV")
        self.rbMaximizeEV.setObjectName(u"rbMaximizeEV")
        self.rbMaximizeEV.setText(u"Maximize")
        self.radioGroupEV.addButton(self.rbDefaultEV)
        self.radioGroupEV.addButton(self.rbRandomizeEV)
        self.radioGroupEV.addButton(self.rbMaximizeEV)
        self.groupEVLayout.addWidget(self.rbDefaultEV)
        self.groupEVLayout.addWidget(self.rbRandomizeEV)
        self.groupEVLayout.addWidget(self.rbMaximizeEV)
        ### Moves
        self.groupMoves = QGroupBox(self.oWidget)
        self.groupMoves.setObjectName(u"groupMoves")
        self.groupMoves.setTitle(u"Moves")
        self.groupRndLayout.addWidget(self.groupMoves)
        self.groupMovesLayout = QHBoxLayout(self.groupMoves)
        self.groupMovesLayout.setObjectName(u"groupMovesLayout")
        self.groupMoves.setLayout(self.groupMovesLayout)
        #### Moves encounters
        self.cbMovesEnc = QCheckBox(self.groupMoves)
        self.cbMovesEnc.setObjectName(u"cbMovesEnc")
        self.cbMovesEnc.setText(u"Encounters")
        self.groupMovesLayout.addWidget(self.cbMovesEnc)
        #### Moves trainers
        self.cbMovesTrainers = QCheckBox(self.groupMoves)
        self.cbMovesTrainers.setObjectName(u"cbMovesTrainers")
        self.cbMovesTrainers.setText(u"Trainers")
        self.groupMovesLayout.addWidget(self.cbMovesTrainers)
        #### Moves tower trainers
        self.cbMovesTowerTrainers = QCheckBox(self.groupMoves)
        self.cbMovesTowerTrainers.setObjectName(u"cbMovesTowerTrainers")
        self.cbMovesTowerTrainers.setText(u"Tower trainers")
        self.groupMovesLayout.addWidget(self.cbMovesTowerTrainers)
        ### Abilities
        self.groupAbilities = QGroupBox(self.oWidget)
        self.groupAbilities.setObjectName(u"groupAbilities")
        self.groupAbilities.setTitle(u"Abilities")
        self.groupRndLayout.addWidget(self.groupAbilities)
        self.groupAbilitiesLayout = QHBoxLayout(self.groupAbilities)
        self.groupAbilitiesLayout.setObjectName(u"groupAbilitiesLayout")
        self.groupAbilities.setLayout(self.groupAbilitiesLayout)
        #### Abilities encounters
        self.cbAbilitiesEnc = QCheckBox(self.groupAbilities)
        self.cbAbilitiesEnc.setObjectName(u"cbAbilitiesEnc")
        self.cbAbilitiesEnc.setText(u"Encounters")
        self.groupAbilitiesLayout.addWidget(self.cbAbilitiesEnc)
        #### Abilities trainers
        self.cbAbilitiesTrainers = QCheckBox(self.groupAbilities)
        self.cbAbilitiesTrainers.setObjectName(u"cbAbilitiesTrainers")
        self.cbAbilitiesTrainers.setText(u"Trainers")
        self.groupAbilitiesLayout.addWidget(self.cbAbilitiesTrainers)
        #### Abilities tower trainers
        self.cbAbilitiesTowerTrainers = QCheckBox(self.groupAbilities)
        self.cbAbilitiesTowerTrainers.setObjectName(u"cbAbilitiesTowerTrainers")
        self.cbAbilitiesTowerTrainers.setText(u"Tower trainers")
        self.groupAbilitiesLayout.addWidget(self.cbAbilitiesTowerTrainers)
        ### HeldItems
        self.groupHeldItems = QGroupBox(self.oWidget)
        self.groupHeldItems.setObjectName(u"groupHeldItems")
        self.groupHeldItems.setTitle(u"Held items")
        self.groupRndLayout.addWidget(self.groupHeldItems)
        self.groupHeldItemsLayout = QHBoxLayout(self.groupHeldItems)
        self.groupHeldItemsLayout.setObjectName(u"groupHeldItemsLayout")
        self.groupHeldItems.setLayout(self.groupHeldItemsLayout)
        #### HeldItems encounters
        self.cbHeldItemsEnc = QCheckBox(self.groupHeldItems)
        self.cbHeldItemsEnc.setObjectName(u"cbHeldItemsEnc")
        self.cbHeldItemsEnc.setText(u"Encounters")
        self.groupHeldItemsLayout.addWidget(self.cbHeldItemsEnc)
        #### HeldItems trainers
        self.cbHeldItemsTrainers = QCheckBox(self.groupHeldItems)
        self.cbHeldItemsTrainers.setObjectName(u"cbHeldItemsTrainers")
        self.cbHeldItemsTrainers.setText(u"Trainers")
        self.groupHeldItemsLayout.addWidget(self.cbHeldItemsTrainers)
        #### HeldItems tower trainers
        self.cbHeldItemsTowerTrainers = QCheckBox(self.groupHeldItems)
        self.cbHeldItemsTowerTrainers.setObjectName(u"cbHeldItemsTowerTrainers")
        self.cbHeldItemsTowerTrainers.setText(u"Tower trainers")
        self.groupHeldItemsLayout.addWidget(self.cbHeldItemsTowerTrainers)
        ### Scale options
        self.groupScale = QGroupBox(self.oWidget)
        self.groupScale.setObjectName(u"groupScale")
        self.groupScale.setTitle(u"Pokémon Scale Options")
        self.groupRndLayout.addWidget(self.groupScale)
        self.groupScaleLayout = QHBoxLayout(self.groupScale)
        self.groupScaleLayout.setObjectName(u"groupScaleLayout")
        self.groupScale.setLayout(self.groupScaleLayout)
        ##### Scale default & 1:1 & random
        self.radioGroupEV = QButtonGroup(self.groupScale)
        self.rbDefaultScale = QRadioButton("Scale")
        self.rbDefaultScale.setObjectName(u"rbDefaultScale")
        self.rbDefaultScale.setText(u"Default")
        self.rbDefaultScale.setChecked(True)
        self.rbNaturalScale = QRadioButton("Scale")
        self.rbNaturalScale.setObjectName(u"rbNaturalScale")
        self.rbNaturalScale.setText(u"1:1 Scale")
        self.rbRandomizeScale = QRadioButton("Scale")
        self.rbRandomizeScale.setObjectName(u"rbRandomizeScale")
        self.rbRandomizeScale.setText(u"Randomize")
        self.radioGroupEV.addButton(self.rbDefaultScale)
        self.radioGroupEV.addButton(self.rbNaturalScale)
        self.radioGroupEV.addButton(self.rbRandomizeScale)
        self.groupScaleLayout.addWidget(self.rbDefaultScale)
        self.groupScaleLayout.addWidget(self.rbNaturalScale)
        self.groupScaleLayout.addWidget(self.rbRandomizeScale)

        # Set Utils
        ## Level options
        self.groupLvl = QGroupBox(self.uWidget)
        self.groupLvl.setObjectName(u"groupLvl")
        self.groupLvl.setTitle(u"Level Options")
        self.uLayout.addWidget(self.groupLvl)
        self.groupLvlLayout = QVBoxLayout(self.groupLvl)
        self.groupLvlLayout.setObjectName(u"groupLvlLayout")
        self.groupLvl.setLayout(self.groupLvlLayout)
        ### Level group decrease/increase
        self.groupLvlModifier = QGroupBox(self.uWidget)
        self.groupLvlModifier.setObjectName(u"groupLvlModifier")
        self.groupLvlModifier.setTitle(u"Modifier")
        self.groupLvlLayout.addWidget(self.groupLvlModifier)
        self.groupLvlModifierLayout = QVBoxLayout(self.groupLvlModifier)
        self.groupLvlModifierLayout.setObjectName(u"groupLvlModifierLayout")
        self.groupLvlModifier.setLayout(self.groupLvlModifierLayout)
        ### Level group radio
        self.groupLvlFP = QGroupBox(self.groupLvlModifier)
        self.groupLvlFP.setObjectName(u"groupLvlFP")
        self.groupLvlFP.setFlat(True)
        self.groupLvlModifierLayout.addWidget(self.groupLvlFP)
        self.groupLvlFPLayout = QHBoxLayout(self.groupLvlFP)
        self.groupLvlFPLayout.setObjectName(u"groupLvlFPLayout")
        self.groupLvlFP.setLayout(self.groupLvlFPLayout)
        #### Level radio
        self.radioGroupLvl = QButtonGroup(self.groupLvlFP)
        self.rbFlatLvl = QRadioButton("EV")
        self.rbFlatLvl.setObjectName(u"rbFlatLvl")
        self.rbFlatLvl.setText(u"Flat")
        self.rbFlatLvl.setChecked(True)
        self.rbPercentLvl = QRadioButton("EV")
        self.rbPercentLvl.setObjectName(u"rbPercentLvl")
        self.rbPercentLvl.setText(u"Percentage")
        self.rbMaximizeEV = QRadioButton("EV")
        self.rbMaximizeEV.setObjectName(u"rbMaximizeEV")
        self.rbMaximizeEV.setText(u"Maximize")
        self.radioGroupLvl.addButton(self.rbFlatLvl)
        self.radioGroupLvl.addButton(self.rbPercentLvl)
        self.groupLvlFPLayout.addWidget(self.rbFlatLvl)
        self.groupLvlFPLayout.addWidget(self.rbPercentLvl)
        ### Level group decrease/increase
        self.groupLvlDecInc = QGroupBox(self.groupLvlModifier)
        self.groupLvlDecInc.setObjectName(u"groupLvlDecInc")
        self.groupLvlDecInc.setFlat(True)
        self.groupLvlModifierLayout.addWidget(self.groupLvlDecInc)
        self.groupLvlDecIncLayout = QHBoxLayout(self.groupLvlDecInc)
        self.groupLvlDecIncLayout.setObjectName(u"groupLvlDecIncLayout")
        self.groupLvlDecInc.setLayout(self.groupLvlDecIncLayout)
        #### Level group decrease
        self.groupLvlDec = QGroupBox(self.groupLvlDecInc)
        self.groupLvlDec.setObjectName(u"groupLvlDec")
        self.groupLvlDecIncLayout.addWidget(self.groupLvlDec)
        self.groupLvlDecLayout = QHBoxLayout(self.groupLvlDec)
        self.groupLvlDecLayout.setObjectName(u"groupLvlDecLayout")
        self.groupLvlDec.setLayout(self.groupLvlDecLayout)
        ##### Level decrease
        self.labelLvlDec = QLabel(self.groupLvlDec)
        self.labelLvlDec.setObjectName(u"labelLvlDec")
        self.labelLvlDec.setText(u"Decrease")
        self.groupLvlDecLayout.addWidget(self.labelLvlDec)
        self.sbLvlDec = QSpinBox(self.groupLvlDec)
        self.sbLvlDec.setObjectName(u"sbLvlDec")
        self.sbLvlDec.setFixedSize(QSize(42, 22))
        self.sbLvlDec.setMinimum(0)
        self.sbLvlDec.setMaximum(100)
        self.groupLvlDecLayout.addWidget(self.sbLvlDec)
        #### Level group increase
        self.groupLvlInc = QGroupBox(self.groupLvlDecInc)
        self.groupLvlInc.setObjectName(u"groupLvlInc")
        self.groupLvlDecIncLayout.addWidget(self.groupLvlInc)
        self.groupLvlIncLayout = QHBoxLayout(self.groupLvlInc)
        self.groupLvlIncLayout.setObjectName(u"groupLvlIncLayout")
        self.groupLvlInc.setLayout(self.groupLvlIncLayout)
        ##### Level increase
        self.labelLvlInc = QLabel(self.groupLvlInc)
        self.labelLvlInc.setObjectName(u"labelLvlInc")
        self.labelLvlInc.setText(u"Increase")
        self.groupLvlIncLayout.addWidget(self.labelLvlInc)
        self.sbLvlInc = QSpinBox(self.groupLvlInc)
        self.sbLvlInc.setObjectName(u"sbLvlInc")
        self.sbLvlInc.setFixedSize(QSize(42, 22))
        self.sbLvlInc.setMinimum(0)
        self.sbLvlInc.setMaximum(100)
        self.groupLvlIncLayout.addWidget(self.sbLvlInc)
        ### Level group min/max
        self.groupLvlMinMax = QGroupBox(self.uWidget)
        self.groupLvlMinMax.setObjectName(u"groupLvlMinMax")
        self.groupLvlMinMax.setTitle(u"Cap")
        self.groupLvlLayout.addWidget(self.groupLvlMinMax)
        self.groupLvlMinMaxLayout = QHBoxLayout(self.groupLvlMinMax)
        self.groupLvlMinMaxLayout.setObjectName(u"groupLvlMinMaxLayout")
        self.groupLvlMinMax.setLayout(self.groupLvlMinMaxLayout)
        #### Level group min
        self.groupLvlMin = QGroupBox(self.groupLvlMinMax)
        self.groupLvlMin.setObjectName(u"groupLvlMin")
        self.groupLvlMinMaxLayout.addWidget(self.groupLvlMin)
        self.groupLvlMinLayout = QHBoxLayout(self.groupLvlMin)
        self.groupLvlMinLayout.setObjectName(u"groupLvlMinLayout")
        self.groupLvlMin.setLayout(self.groupLvlMinLayout)
        ##### Level min
        self.labelLvlMin = QLabel(self.groupLvlMin)
        self.labelLvlMin.setObjectName(u"labelLvlMin")
        self.labelLvlMin.setText(u"Min")
        self.groupLvlMinLayout.addWidget(self.labelLvlMin)
        self.sbLvlMin = QSpinBox(self.groupLvlMin)
        self.sbLvlMin.setObjectName(u"sbLvlMin")
        self.sbLvlMin.setFixedSize(QSize(42, 22))
        self.sbLvlMin.setMinimum(1)
        self.sbLvlMin.setMaximum(100)
        self.groupLvlMinLayout.addWidget(self.sbLvlMin)
        #### Level group max
        self.groupLvlMax = QGroupBox(self.groupLvlMinMax)
        self.groupLvlMax.setObjectName(u"groupLvlMax")
        self.groupLvlMinMaxLayout.addWidget(self.groupLvlMax)
        self.groupLvlMaxLayout = QHBoxLayout(self.groupLvlMax)
        self.groupLvlMaxLayout.setObjectName(u"groupLvlMaxLayout")
        self.groupLvlMax.setLayout(self.groupLvlMaxLayout)
        ##### Level max
        self.labelLvlMax = QLabel(self.groupLvlMax)
        self.labelLvlMax.setObjectName(u"labelLvlMax")
        self.labelLvlMax.setText(u"Max")
        self.groupLvlMaxLayout.addWidget(self.labelLvlMax)
        self.sbLvlMax = QSpinBox(self.groupLvlMax)
        self.sbLvlMax.setObjectName(u"sbLvlMax")
        self.sbLvlMax.setFixedSize(QSize(42, 22))
        self.sbLvlMax.setMinimum(1)
        self.sbLvlMax.setMaximum(100)
        self.sbLvlMax.setValue(100)
        self.groupLvlMaxLayout.addWidget(self.sbLvlMax)


        # Set Image
        self.imgLabel = QLabel(self.cWidget)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setFixedSize(QSize(320,180))
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setPixmap(QPixmap("image.png"))
        self.cLayout.addWidget(self.imgLabel)
        # Set Console
        self.console = QTextEdit(self.cWidget)
        self.console.setObjectName(u"console")
        self.console.setFixedWidth(320)
        self.console.setReadOnly(True)
        self.cLayout.addWidget(self.console)
        # Set Activation Button
        self.btnStart = QPushButton(self.cWidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.move(740, 770)
        self.btnStart.setFixedSize(QSize(320, 125))
        self.btnStart.setText(u"Start!")
        self.cLayout.addWidget(self.btnStart)

        self.resize(self.mLayout.sizeHint())

        self.btnStart.clicked.connect(self.start)
        return

    def initValues(self):
        self.param = {
            "romfspath": "",
            "gen": [],
            "leg": True,
            "r": {
                "starters": False,
                "evolutions": False,
                "types": False,
                "eggmoves": False,
                "egggroups": False,
                "enc" : {
                    "field": False,
                    "safari": False,
                    "underground": False
                },
                "trainers": {
                    "items": False,
                    "field": False,
                    "tower": False,
                    "iv": 0, # 0 default, 1 randomize, 2 maximize
                    "ev": 0, # 0 default, 1 randomize, 2 maximize
                },
                "moves": {
                    "enc": False,
                    "trainers": False,
                    "tower": False
                },
                "abilities": {
                    "enc": False,
                    "trainers": False,
                    "tower": False
                },
                "helditems": {
                    "enc": False,
                    "trainers": False,
                    "tower": False
                }
            },
            "scaling": 0, # 0 default, 1 natural scale, 2 randomize
            "level": {
                "modifier": 0, # 0 flat, 1 percent
                "decrease": 0,
                "increase": 0,
                "minimum": 1,
                "maximum": 100
            }
        }

    def start(self):
        self.dialog = QFileDialog()
        romFSPath = self.dialog.getExistingDirectory(self, "Select ROMFS path")

        if path.exists(path.join(romFSPath, "Data")):
            romFSPath = path.join(romFSPath, "Data")
        
        if romFSPath == "": 
            self.console.append("ROMFS Directory can not be empty")
            return

        self.param["romfspath"] = romFSPath
        self.console.append("ROMFS Directory set to " + romFSPath)
        self.setValues()

        # Now let's shake our mod
        Main.Main(self.console, self.param)
        return

    def setValues(self):
        if self.cbGen1.isChecked(): self.param["gen"].append(1)
        if self.cbGen2.isChecked(): self.param["gen"].append(2)
        if self.cbGen3.isChecked(): self.param["gen"].append(3)
        if self.cbGen4.isChecked(): self.param["gen"].append(4)
        if self.cbLeg.isChecked(): self.param["leg"] = True

        if self.cbStarters.isChecked(): self.param["r"]["starters"] = True
        if self.cbEvolutions.isChecked(): self.param["r"]["evolutions"] = True
        if self.cbTypes.isChecked(): self.param["r"]["types"] = True
        if self.cbEggMoves.isChecked(): self.param["r"]["eggmoves"] = True
        if self.cbEggGroups.isChecked(): self.param["r"]["egggroups"] = True

        if self.cbEncField.isChecked(): self.param["r"]["enc"]["field"] = True
        if self.cbEncSafari.isChecked(): self.param["r"]["enc"]["safari"] = True
        if self.cbEncUg.isChecked(): self.param["r"]["enc"]["underground"] = True

        if self.cbTrainersItems.isChecked(): self.param["r"]["trainers"]["items"] = True
        if self.cbTrainersField.isChecked(): self.param["r"]["trainers"]["field"] = True
        if self.cbTrainersTower.isChecked(): self.param["r"]["trainers"]["tower"] = True
        if self.rbDefaultIV.isChecked(): self.param["r"]["trainers"]["iv"] = 0
        if self.rbRandomizeIV.isChecked(): self.param["r"]["trainers"]["iv"] = 1
        if self.rbMaximizeIV.isChecked(): self.param["r"]["trainers"]["iv"] = 2
        if self.rbDefaultEV.isChecked(): self.param["r"]["trainers"]["ev"] = 0
        if self.rbRandomizeEV.isChecked(): self.param["r"]["trainers"]["ev"] = 1
        if self.rbMaximizeEV.isChecked(): self.param["r"]["trainers"]["ev"] = 2

        if self.cbMovesEnc.isChecked(): self.param["r"]["moves"]["enc"] = True
        if self.cbMovesTrainers.isChecked(): self.param["r"]["moves"]["trainers"] = True
        if self.cbMovesTowerTrainers.isChecked(): self.param["r"]["moves"]["tower"] = True

        if self.cbAbilitiesEnc.isChecked(): self.param["r"]["abilities"]["enc"] = True
        if self.cbAbilitiesTrainers.isChecked(): self.param["r"]["abilities"]["trainers"] = True
        if self.cbAbilitiesTowerTrainers.isChecked(): self.param["r"]["abilities"]["tower"] = True

        if self.cbHeldItemsEnc.isChecked(): self.param["r"]["helditems"]["enc"] = True
        if self.cbHeldItemsTrainers.isChecked(): self.param["r"]["helditems"]["trainers"] = True
        if self.cbHeldItemsTowerTrainers.isChecked(): self.param["r"]["helditems"]["tower"] = True

        if self.rbDefaultScale.isChecked(): self.param["scaling"] = 0
        if self.rbNaturalScale.isChecked(): self.param["scaling"] = 1
        if self.rbRandomizeScale.isChecked(): self.param["scaling"] = 2

        if self.rbFlatLvl.isChecked(): self.param["level"]["modifier"] = 0
        if self.rbPercentLvl.isChecked(): self.param["level"]["modifier"] = 1
        self.param["level"]["decrease"] = self.sbLvlDec.value()
        self.param["level"]["increase"] = self.sbLvlInc.value()
        self.param["level"]["minimum"] = self.sbLvlMin.value()
        self.param["level"]["maximum"] = self.sbLvlMax.value()
        return



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion") # Best style by far

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(42, 42, 42))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(20, 20, 25))
    palette.setColor(QPalette.AlternateBase, QColor(0, 0, 0))
    # palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
    # palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
    # palette.setColor(QPalette.PlaceholderText, QColor(0, 0, 0))
    palette.setColor(QPalette.Text, QColor(150, 200, 255))
    palette.setColor(QPalette.Button, QColor(80, 20, 20))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
    # palette.setColor(QPalette.Link, QColor(0, 0, 0))
    # palette.setColor(QPalette.LinkVisited, QColor(0, 0, 0))
    palette.setColor(QPalette.Highlight, QColor(100,100,100))
    palette.setColor(QPalette.HighlightedText, QColor(200, 222, 255))
    app.setPalette(palette)

    window = App()
    window.show()
    sys.exit(app.exec_())