# NEURON-Based Nerve Bundle Model

## Introduction
This project aims to develop a simplified nerve bundle model using the **NEURON** simulation environment to study the effect of **Electrode** to **Compound Action Potential (CAP)**.

The model will begin with a **single nerve fiber** and progressively advance to a more complex **nerve bundle**. The stimulation methodology transitions from Patch Clamp to Point Electrode and ultimately to Surface Electrode. Recording techniques will evolve from Patch Clamp to Extracellular Patch.

The model will focus on **Axon**, omitting soma, dendritic structures, and neurotransmitter-mediated synaptic transmission.

## Procedure
The project is divided into five distinct phases:
- **Phase I**: ***Single neuron fiber***, stimulation and recording via Patch Clamp.
- **Phase II**: Single neuron fiber, stimulation via Patch Clamp, recording via ***Extracellular Patch***.
- **Phase III**: Single neuron fiber, stimulation via ***Point Electrode*** (considering the distance between electrode and fiber), recording via Extracellular Patch.
- **Phase IV**: ***Nerve fiber bundle*** (considering fiber diameter variability), stimulation via Point Electrode (considering distance), recording via Extracellular Patch.
- **Phase V**: Nerve fiber bundle (considering fiber diameter variability), stimulation via ***Surface Electrode*** (considering charge density), recording via Extracellular Patch.

![alt text](PhaseI-III.png)
![alt text](PhaseIV.png)
![alt text](PhaseV.png)

## Implementation
### Programming Language
The model will be implemented using the **hoc** and **python** programming language.

### File Architecture
- Topology: Definition of the modeled nerve fiber and nerve bundle structures.
- Stimulation: Implementation of various stimulation methods across different phases.
- Record: Implementation of different recording methods and data acquisition approaches.

## Outcome
The expected results from this project include:
- A stepwise approach to constructing a comprehensive CAP model.
- Insights into the effect of stimulation methods and electrode placement on signal propagation.
- A foundational framework for further extensions incorporating more physiological complexities.