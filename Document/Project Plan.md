# NEURON-Based Nerve Bundle Model

## 1. Introduction
This project aims to develop a simplified nerve bundle model using the **NEURON** simulation environment to study the effect of **Electrode** to **Compound Action Potential (CAP)**.

The model will begin with a **single nerve fiber** and progressively advance to a more complex **nerve bundle**. The stimulation methodology transitions from **intracellular** electrode to extracellular electrode (only considering the **distance** between electrode and fiber) and ultimately to extracellular electrode (considering both distance and **membrane area**). Recording techniques will evolve from **intracellular** electrode to **extracellular** electrode.

## 2. Scope
The scope of this project includes a topological representation of peripheral nerves as a linear single and multi-axon group of multi diameters, myelinated and unmyelinated fibers. This comprises stimulation waveforms, locations, recording modalities and sites. Soma, dendrites and synapses are out of scope. <br/>



## 3. Procedure
The project is divided into five distinct phases:<br/>
- **3.1 Phase I**: Single neuron fiber, stimulation and recording via intracellular electrode.<br/>
- **3.2 Phase II**: Single neuron fiber, stimulation via extracellular electrode (considering distance), recording via intracellular electrode.<br/>
- **3.3 Phase III**: Single neuron fiber, stimulation via extracellular electrode, recording via extracellular electrode.<br/>
- **3.4 Phase IV**: Nerve fiber bundle (considering fiber diameter variability), stimulation via extracellular electrode, recording via extracellular electrode.<br/>
- **3.5 Phase V**: Nerve fiber bundle, stimulation via extracellular electrode (considering charge density to each fiber), recording via extracellular electrode.<br/>

## 4. Schedule
|Procedure|Nerve|Stimulation|Record|Date|.<br/>
|-|-|-|-|-|.<br/>
|Phase I|Single|Intracellular|Intracellular|2025.03.05|<br/>
|Phase II|Single|Extracellular (distance)|Intracellular|2025.03.07|<br/>
|Phase III|Single|Extracellular (distance)|Extracellular|2025.03.11|<br/>
|Phase IV|Multiple|Extracellular (distance)|Extracellular|2025.03.12|<br/>
|Phase V|Multiple|Extracellular (charge density)|Extracellular|2025.03.13|<br/>

![alt text](PhaseI-III.png)
![alt text](PhaseIV.png)
![alt text](PhaseV.png)

## 5. Implementation
### 5.1 Programming Languages
The model will be implemented using the **hoc** and **Python** programming language.

### 5.2 File Architecture
- **Topology**: Definition of the modeled nerve fiber and nerve bundle structures.
- **Stimulation**: Implementation of various stimulation methods across different phases.
- **Record**: Implementation of different recording methods and data acquisition approaches.

## 6. Stimulation
### 6.1 Waveform
The simulation will incorporate different waveforms, including:<br/>
- **Single pulse stimulation**: A single short-duration stimulus.<br/>
- **Biphasic pulse stimulation**: Biphasic waveform with active and passive charge receovery.

### 6.2 Parameters
Each stimulation will be configured with different parameters:<br/>
- **Amplitude**: 0 mA to 5mA<br/>
- **Duration**: 0 µs to 2,000 µs<br/>
- **Waveform Type**: Square pulse, Biphasic pulse, Sinusoidal<br/>
- **Electrode-fiber distance**: 1 to 20 µm<br/>
- **Fiber diameter**: 0.2 to 1.5 µm<br/>

## 7. Recording
Rercording will start from a single fiber axon and single action potential AP to multi-fiber model compound ation potential CAP.<br/>
- **Intracellular electrode**: PatchClamp intracellular potential changes.<br/>
- **Extracellular electrode**: Measures the extracellular potential changes.<br/>
- **Compound action potential**: Sum the synchronos action potentials of different nerve fibers.

## 8. Outcome
The expected results from this project include:<br/>
- A nerve boundle model built with hoc file.<br/>
- Some figures and animations which show the compound action potential.<br/>
- A document show how to use the model.