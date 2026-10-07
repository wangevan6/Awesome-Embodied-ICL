# Awesome In-context learning for Embodied AI system — Paper catalogue

Our manuscript, *In-Context Learning for Embodied Agents: Methods, Benchmarks, and Open Challenges*, defines this catalogue’s context forms and roles. All 412 references imported from the external survey *In-Context Learning for Robots: Methods and Applications* are retained, including parameter-adaptation comparisons. The two surveys have independent reference numbering.

Entries are grouped by their first listed context form; roles are independent and may overlap. Roadmap examples about broader domains and evaluation have a separate group; all other works await mapping. Each entry preserves its external reference number, citation, source URL, original group, and bibliography pages. The 21 annotated entries add reading notes supported by explicit survey pages. An unannotated entry has no inferred context budget, deployment update regime, or experimental result.

Method years follow Appendix A's first public year; supporting-reference years use the bibliography date. Both dates are shown when they differ. Source URLs are transcribed from the PDF and have not been independently verified for availability.

**External inventory snapshot:** [inventory and provenance](data/survey-references.json) · [external survey PDF, arXiv v1](https://arxiv.org/pdf/2609.36012v1) · SHA-256 of the extracted copy `49ac471603c28c81d01ff749d8256f9b9d5ad0c30bd358dba979dbb2feb8b0a9`.

**Conceptual authority:** our manuscript’s roadmap (Figure 2) · [full roadmap mapping](data/manuscript-mapping.json) · [source identities](data/sources.json). The roadmap includes 29 further works outside the external inventory; those remain recorded in the mapping data, including RoboSSM.

## Text context

3 references.

<a id="ref-163"></a>
### External [163] StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** S. Xu, Y. Wang, Z. Wang, D. Zhu, C. Xia, C. Du, D. Liu, T. Huang, and C. Xu. StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models. arXiv preprint arXiv:2608.11671, 2026. URL https://arxiv.org/abs/2608.11671.

**Our manuscript [20]:** roadmap, Figure 2. **Form:** Text, Multimodal. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.11671) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="kat-2024"></a>
### External [15] Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** N. Di Palo and E. Johns. Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics. arXiv preprint arXiv:2403.19578, 2024. URL https://arxiv.org/abs/2403.19578.

**Our manuscript [13]:** roadmap, Figure 2. **Form:** Text. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2403.19578) — transcribed from the external survey.

**Reading-note evidence:** [p. 18](https://arxiv.org/pdf/2609.36012v1#page=18), [p. 19](https://arxiv.org/pdf/2609.36012v1#page=19), [p. 20](https://arxiv.org/pdf/2609.36012v1#page=20).

- **Deployment context:** keypoint–action examples available before rollout
- **Action mechanism:** encodes keypoint and action records for inference with a text-pretrained model
- **Deployment weights:** frozen
- **Setting discussed:** teaching-budget comparison with KeyAct-DP
- **Survey evidence:** The survey reports that contextual inference is competitive with few examples, while policy training becomes stronger with more; the crossover changes with representation.
- **Why read it:** Shows that the useful demonstration budget depends jointly on representation and adaptation mechanism.
- **Adaptation target:** demonstrated task behavior
- **Evidence description:** teaching-budget comparison
- **Interpretation limit:** Keypoint representation and the comparison policy affect the crossover; the result is not a general claim that frozen inference always beats training.

<a id="roboprompt-2024"></a>
### External [153] In-Context Learning Enables Robot Action Prediction in LLMs (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** Y. Yin, Z. Wang, Y. Sharma, D. Niu, T. Darrell, and R. Herzig. In-Context Learning Enables Robot Action Prediction in LLMs. arXiv preprint arXiv:2410.12782, 2024. URL https://arxiv.org/abs/2410.12782.

**Our manuscript [21]:** roadmap, Figure 2. **Form:** Text. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2410.12782) — transcribed from the external survey.

**Reading-note evidence:** [p. 15](https://arxiv.org/pdf/2609.36012v1#page=15), [p. 18](https://arxiv.org/pdf/2609.36012v1#page=18), [p. 20](https://arxiv.org/pdf/2609.36012v1#page=20).

- **Deployment context:** numerical object poses and keyframe end-effector action examples serialized for a language model
- **Action mechanism:** a frozen language model parses structured examples and predicts robot actions
- **Deployment weights:** frozen
- **Setting discussed:** textual action inference using structured robot state and demonstrations
- **Survey evidence:** The survey identifies object poses and keyframe end-effector actions as the interface through which a text-pretrained model receives robot examples.
- **Why read it:** Exposes the coordinate and representation work required to make language-model outputs physically meaningful.
- **Adaptation target:** action interpretation from structured examples
- **Evidence description:** method discussion in survey
- **Interpretation limit:** The interface depends on perception, coordinate conventions, and action representations; it is not raw-image prompting alone.

## Visual context

6 references.

<a id="ref-23"></a>
### External [23] HOST: Robots Acquire Manipulation Skills in Seconds from a Single Human Video (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** G. Chen, M. Wang, T. Cui, Z. Zhou, Q. Shao, S. Li, et al. HOST: Robots Acquire Manipulation Skills in Seconds from a Single Human Video. arXiv preprint arXiv:2607.20033, 2026. URL https://arxiv.org/abs/2607.20033.

**Our manuscript [31]:** roadmap, Figure 2. **Form:** Visual. **Role:** Task specification.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.20033) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="zero-wam-2026"></a>
### External [24] Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** J. Zhou, Q. Zhang, G. Xu, C. Fan, Y. Zhao, R. Wang, et al. Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization. arXiv preprint arXiv:2608.26103, 2026. URL https://arxiv.org/abs/2608.26103.

**Our manuscript [10]:** roadmap, Figure 2. **Form:** Visual. **Role:** Task specification.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.26103) — transcribed from the external survey.

**Reading-note evidence:** [p. 11](https://arxiv.org/pdf/2609.36012v1#page=11), [p. 24](https://arxiv.org/pdf/2609.36012v1#page=24), [p. 25](https://arxiv.org/pdf/2609.36012v1#page=25), [p. 26](https://arxiv.org/pdf/2609.36012v1#page=26), [p. 30](https://arxiv.org/pdf/2609.36012v1#page=30).

- **Deployment context:** human demonstration video and recent robot observation history
- **Action mechanism:** a video model generates a future clip that conditions the action model during deployment
- **Deployment weights:** frozen
- **Setting discussed:** human-video-conditioned world-action control
- **Survey evidence:** Figure 11 explicitly shows both video and action branches frozen at deployment, with generated future video replacing recorded future video.
- **Why read it:** Retains a predicted future on the deployed action path, separating it from auxiliary future supervision.
- **Adaptation target:** task procedure conveyed by human video
- **Evidence description:** deployment architecture in survey
- **Interpretation limit:** The predicted future must preserve the demonstrated procedure and remain physically realizable. Detailed evaluation protocols require the primary paper.

<a id="ref-99"></a>
### External [99] Introducing S1: In-Context Learning for Robotics (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** Skild AI. Introducing S1: In-Context Learning for Robotics. Skild AI official blog, 2026. URL https://www.skild.ai/blogs/s1. Accessed September 19, 2026. Industrial technical report.

**Our manuscript [33]:** roadmap, Figure 2. **Form:** Visual. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://www.skild.ai/blogs/s1) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-14"></a>
### External [14] Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** V. Jain, M. Attarian, N. J. Joshi, A. Wahid, D. Driess, Q. Vuong, et al. Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers. arXiv preprint arXiv:2403.12943, 2024. URL https://arxiv.org/abs/2403.12943.

**Our manuscript [27]:** roadmap, Figure 2. **Form:** Visual. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2403.12943) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-83"></a>
### External [83] Vision Language Models are In-Context Value Learners (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** Y. J. Ma, J. Hejna, A. Wahid, C. Fu, D. Shah, J. Liang, Z. Xu, S. Kirmani, P. Xu, D. Driess, T. Xiao, J. Tompson, O. Bastani, D. Jayaraman, W. Yu, T. Zhang, D. Sadigh, and F. Xia. Vision Language Models are In-Context Value Learners, 2024. URL https://arxiv.org/abs/2411.04549.

**Our manuscript [28]:** roadmap, Figure 2. **Form:** Visual. **Role:** State representation.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2411.04549) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-148"></a>
### External [148] BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** E. Jang, A. Irpan, M. Khansari, D. Kappler, F. Ebert, C. Lynch, et al. BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning. arXiv preprint arXiv:2202.02005, 2022. URL https://arxiv.org/abs/2202.02005.

**Our manuscript [26]:** roadmap, Figure 2. **Form:** Visual. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2202.02005) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

## Trajectory context

19 references.

<a id="ref-10"></a>
### External [10] RoboTTT: Context Scaling for Robot Policies (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** Y. Jiang, Y. Chebotar, R. Zheng, F. Hu, Y. Ge, J. Wu, et al. RoboTTT: Context Scaling for Robot Policies. arXiv preprint arXiv:2607.15275, 2026. URL https://arxiv.org/abs/2607.15275.

**Our manuscript [9]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.15275) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="icwm-2026"></a>
### External [41] In-Context World Modeling for Robotic Control (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** S. Wang, J. Shi, S. Fei, Z. Fu, L. Ji, J. Gong, and X. Qiu. In-Context World Modeling for Robotic Control. arXiv preprint arXiv:2606.26025, 2026. URL https://arxiv.org/abs/2606.26025.

**Our manuscript [52]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** State representation.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.26025) — transcribed from the external survey.

**Reading-note evidence:** [p. 11](https://arxiv.org/pdf/2609.36012v1#page=11), [p. 19](https://arxiv.org/pdf/2609.36012v1#page=19), [p. 32](https://arxiv.org/pdf/2609.36012v1#page=32).

- **Deployment context:** task-agnostic probes that reveal action effects before task execution
- **Action mechanism:** infers physical context from transitions and conditions an action policy directly
- **Deployment weights:** frozen
- **Setting discussed:** adaptation to changes in observation and embodiment
- **Survey evidence:** The survey identifies ICWM as physical-context inference from probes; its inferred representation directly conditions the action policy.
- **Why read it:** Distinguishes inferring a present system response from predicting future consequences for control.
- **Adaptation target:** observation and embodiment conditions
- **Evidence description:** method discussion in survey
- **Interpretation limit:** The world-model wording in the title does not make its surveyed deployment interface world-model-based control.

<a id="bpp-2026"></a>
### External [54] Behavior Prompting Policy: Demonstrations as Prompts for Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** A. Patel, B. Pekarek, J. E. C. Hernandez, and S. Song. Behavior Prompting Policy: Demonstrations as Prompts for Manipulation. arXiv preprint arXiv:2606.30457, 2026. URL https://arxiv.org/abs/2606.30457.

**Our manuscript [49]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.30457) — transcribed from the external survey.

**Reading-note evidence:** [p. 18](https://arxiv.org/pdf/2609.36012v1#page=18), [p. 20](https://arxiv.org/pdf/2609.36012v1#page=20), [p. 42](https://arxiv.org/pdf/2609.36012v1#page=42), [p. 43](https://arxiv.org/pdf/2609.36012v1#page=43), [p. 55](https://arxiv.org/pdf/2609.36012v1#page=55).

- **Deployment context:** sensorimotor behavior demonstrations grouped by the intended task
- **Action mechanism:** encodes behavior prompts to condition action decoding
- **Deployment weights:** frozen
- **Setting discussed:** DrawAnything and a three-task laundry study discussed by the survey
- **Survey evidence:** At a fixed 10,000 drawing demonstrations, greater task diversity reduces reported Chamfer error; in the laundry study, language is more reliable than behavior demonstrations.
- **Why read it:** Shows that demonstrations help when they communicate choices of path or order beyond a task label or goal image.
- **Adaptation target:** task-specific procedure and trajectory
- **Evidence description:** drawing and laundry comparisons
- **Interpretation limit:** The benefit depends on what teaching must convey and on training diversity; behavior prompting does not dominate language in every setting.

<a id="ref-77"></a>
### External [77] SynthICL: Scalable In-context Imitation Learning with Synthetic Data (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** C. Qian, R. Fan, Y. Ren, Y. Wang, and E. Johns. SynthICL: Scalable In-context Imitation Learning with Synthetic Data. arXiv preprint arXiv:2606.08154, 2026. URL https://arxiv.org/abs/2606.08154.

**Our manuscript [51]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.08154) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-91"></a>
### External [91] Instant-Fold: In-Context Imitation Learning for Deformable Object Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** Y. Wang, C. Qian, and E. Johns. Instant-Fold: In-Context Imitation Learning for Deformable Object Manipulation. arXiv preprint arXiv:2606.04269, 2026. URL https://arxiv.org/abs/2606.04269.

**Our manuscript [50]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.04269) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-98"></a>
### External [98] GEN-1.5: Embodied Foundation Models are One-Shot Learners (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** Generalist Team. GEN-1.5: Embodied Foundation Models are One-Shot Learners. Generalist AI Blog, August 19, 2026. URL https://generalistai.com/blog/gen-1.5. Accessed September 19, 2026. Industrial technical report.

**Our manuscript [53]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://generalistai.com/blog/gen-1.5) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="iclr-visual-reasoning-2026"></a>
### External [181] ICLR: In-Context Imitation Learning with Visual Reasoning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** T. Nguyen, W. Yuan, S. Wei, H. Li, D. Seita, and Y. Wang. ICLR: In-Context Imitation Learning with Visual Reasoning. arXiv preprint arXiv:2603.07530, 2026. URL https://arxiv.org/abs/2603.07530.

**Our manuscript [48]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.07530) — transcribed from the external survey.

**Reading-note evidence:** [p. 25](https://arxiv.org/pdf/2609.36012v1#page=25), [p. 26](https://arxiv.org/pdf/2609.36012v1#page=26).

- **Deployment context:** demonstration evidence and motion-specific visual reasoning supervision
- **Action mechanism:** gripper-trace supervision shapes action representations; reasoning dropout permits execution without generating those traces
- **Deployment weights:** not detailed in the cited survey passage
- **Setting discussed:** auxiliary predictive supervision for context-conditioned action inference
- **Survey evidence:** The survey discusses this reference alongside SeeTraceAct to distinguish trace supervision from a future prediction required during control.
- **Why read it:** Shows why prediction during training does not by itself imply a predictive deployment interface.
- **Adaptation target:** demonstration-conditioned actions
- **Evidence description:** training/deployment distinction in survey
- **Interpretation limit:** Do not claim that every deployed decision must generate explicit visual reasoning traces; the survey describes a branch that omits them.

<a id="ref-182"></a>
### External [182] SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** J. Son, J. Kim, K. Kam, J. Coholich, S. J. Kim, J. Kim, C. D. Kim, J. Cho, D. Fox, and Z. Kira. SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos, 2026. URL https://arxiv.org/abs/2606.02745.

**Our manuscript [46]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.02745) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-9"></a>
### External [9] In-Context Iterative Policy Improvement for Dynamic Manipulation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** M. Van der Merwe and D. K. Jha. In-Context Iterative Policy Improvement for Dynamic Manipulation. In Conference on Robot Learning, volume 305 of Proceedings of Machine Learning Research, pages 3888–3901, 2025. URL https://proceedings.mlr.press/v305/merwe25a.html.

**Our manuscript [42]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://proceedings.mlr.press/v305/merwe25a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ricl-2025"></a>
### External [17] RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** K. Sridhar, S. Dutta, D. Jayaraman, and I. Lee. RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models. arXiv preprint arXiv:2508.02062, 2025. URL https://arxiv.org/abs/2508.02062.

**Our manuscript [41]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2508.02062) — transcribed from the external survey.

**Reading-note evidence:** [p. 16](https://arxiv.org/pdf/2609.36012v1#page=16), [p. 18](https://arxiv.org/pdf/2609.36012v1#page=18), [p. 20](https://arxiv.org/pdf/2609.36012v1#page=20).

- **Deployment context:** retrieved demonstrations selected for the current query
- **Action mechanism:** retrieval and context encoding condition a learned action generator
- **Deployment weights:** frozen
- **Setting discussed:** adding a demonstration interface to an existing action generator
- **Survey evidence:** The survey contrasts conditioning a generator on retrieved demonstrations with directly returning their recorded actions.
- **Why read it:** Places retrieval in the context-selection stage while the learned generator interprets the example.
- **Adaptation target:** behavior specified by retrieved demonstrations
- **Evidence description:** method discussion in survey
- **Interpretation limit:** Retrieval quality and the generator’s ability to interpret the retrieved evidence are separate sources of generalization.

<a id="ref-30"></a>
### External [30] UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** H. Kim, J. Kang, H. Kang, M. Cho, S. J. Kim, and Y. Lee. UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations, 2025. URL https://arxiv.org/abs/2505.08787.

**Our manuscript [40]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2505.08787) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-159"></a>
### External [159] See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** G. Chen, M. Wang, Q. Shao, Z. Zhou, W. Mao, T. Cui, M. Zhu, Y. Deng, L. Yang, Z. Zhang, Y. Yang, H. Chen, and Y. Yue. See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations, 2025. URL https://arxiv.org/abs/2512.07582.

**Our manuscript [47]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2512.07582) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-245"></a>
### External [245] MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** R. Shah, S. Liu, Q. Wang, Z. Jiang, S. Kumar, M. Seo, et al. MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos. arXiv preprint arXiv:2509.09769, 2025. URL https://arxiv.org/abs/2509.09769.

**Our manuscript [43]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2509.09769) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="icrt-2024"></a>
### External [13] In-Context Imitation Learning via Next-Token Prediction (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** L. Fu, H. Huang, G. Datta, L. Y. Chen, W. C.-H. Panitch, F. Liu, et al. In-Context Imitation Learning via Next-Token Prediction. arXiv preprint arXiv:2408.15980, 2024. URL https://arxiv.org/abs/2408.15980.

**Our manuscript [7]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2408.15980) — transcribed from the external survey.

**Reading-note evidence:** [p. 15](https://arxiv.org/pdf/2609.36012v1#page=15), [p. 18](https://arxiv.org/pdf/2609.36012v1#page=18), [p. 19](https://arxiv.org/pdf/2609.36012v1#page=19), [p. 42](https://arxiv.org/pdf/2609.36012v1#page=42), [p. 43](https://arxiv.org/pdf/2609.36012v1#page=43), [p. 66](https://arxiv.org/pdf/2609.36012v1#page=66).

- **Deployment context:** sensorimotor demonstrations supplying observations and recorded actions, followed by the execution history
- **Action mechanism:** causal sensorimotor sequence modeling reads demonstration evidence and decodes actions without linguistic data
- **Deployment weights:** frozen
- **Setting discussed:** shared test tasks comparing DROID-only and multi-task training data
- **Survey evidence:** The survey reports no progress for the selected DROID-only training condition; multi-task scenes supply different required actions from similar initial observations.
- **Why read it:** Shows why training must make the demonstration informative about the correct continuation.
- **Adaptation target:** task specified by sensorimotor teaching
- **Evidence description:** controlled training-data comparison
- **Interpretation limit:** The cited comparison concerns selected training-data conditions; it does not establish broad cross-embodiment transfer.

<a id="instant-policy-2024"></a>
### External [16] Instant Policy: In-Context Imitation Learning via Graph Diffusion (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** V. Vosylius and E. Johns. Instant Policy: In-Context Imitation Learning via Graph Diffusion. arXiv preprint arXiv:2411.12633, 2024. URL https://arxiv.org/abs/2411.12633.

**Our manuscript [8]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2411.12633) — transcribed from the external survey.

**Reading-note evidence:** [p. 13](https://arxiv.org/pdf/2609.36012v1#page=13), [p. 18](https://arxiv.org/pdf/2609.36012v1#page=18), [p. 19](https://arxiv.org/pdf/2609.36012v1#page=19), [p. 42](https://arxiv.org/pdf/2609.36012v1#page=42).

- **Deployment context:** demonstration geometry and state/action records
- **Action mechanism:** spatial graph representations encode demonstration correspondence before graph-diffusion action generation
- **Deployment weights:** frozen
- **Setting discussed:** manipulation examples with differently shaped boxes in the survey discussion
- **Survey evidence:** The survey uses Instant Policy to show that additional demonstrations can disambiguate the intended task, provided action coordinates and semantics remain compatible.
- **Why read it:** Makes geometric context part of action inference and exposes ambiguity that one demonstration can leave unresolved.
- **Adaptation target:** task interpretation and spatial correspondence
- **Evidence description:** method discussion in survey
- **Interpretation limit:** Additional demonstrations must agree on the intended intervention and use compatible control conventions.

<a id="regent-2024"></a>
### External [154] REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments (2024)

**Date basis:** Appendix A first public year; bibliography publication: 2025. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** K. Sridhar, S. Dutta, D. Jayaraman, and I. Lee. REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments. In International Conference on Learning Representations, 2025. URL https://arxiv.org/abs/2412.04759.

**Our manuscript [39]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2412.04759) — transcribed from the external survey.

**Reading-note evidence:** [p. 16](https://arxiv.org/pdf/2609.36012v1#page=16), [p. 20](https://arxiv.org/pdf/2609.36012v1#page=20).

- **Deployment context:** retrieved demonstration records selected for the current query
- **Action mechanism:** retrieved examples condition a learned action generator; the survey compares this with direct Retrieve-and-Play
- **Deployment weights:** branch-dependent: frozen policy and fine-tuning comparison
- **Setting discussed:** unseen MuJoCo embodiments in the comparison discussed by the survey
- **Survey evidence:** In the surveyed unseen-embodiment comparison, Retrieve-and-Play outperforms the frozen contextual transformer; fine-tuning improves the learned agent.
- **Why read it:** Separates useful retrieved actions from the learned ability to interpret those actions under distribution shift.
- **Adaptation target:** unseen embodiment
- **Evidence description:** simulation comparison
- **Interpretation limit:** The frozen contextual branch and the fine-tuned comparison have different deployment update regimes.

<a id="ref-29"></a>
### External [29] XSkill: Cross Embodiment Skill Discovery (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** M. Xu, Z. Xu, C. Chi, M. Veloso, and S. Song. XSkill: Cross Embodiment Skill Discovery. In Conference on Robot Learning, 2023. URL https://proceedings.mlr.press/v229/xu23a.html.

**Our manuscript [35]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://proceedings.mlr.press/v229/xu23a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-34"></a>
### External [34] DINOBot: Robot Manipulation via Retrieval and Alignment with Vision Foundation Models (2023)

**Date basis:** Appendix A first public year; bibliography publication: 2024. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** N. Di Palo and E. Johns. DINOBot: Robot Manipulation via Retrieval and Alignment with Vision Foundation Models. In IEEE International Conference on Robotics and Automation, 2024. URL https://arxiv.org/abs/2402.13181.

**Our manuscript [37]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2402.13181) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-6"></a>
### External [6] In-context Reinforcement Learning with Algorithm Distillation (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 76](https://arxiv.org/pdf/2609.36012v1#page=76).

**Citation:** M. Laskin, L. Wang, J. Oh, E. Parisotto, S. Spencer, R. Steigerwald, et al. In-context Reinforcement Learning with Algorithm Distillation. arXiv preprint arXiv:2210.14215, 2022. URL https://arxiv.org/abs/2210.14215.

**Our manuscript [12]:** roadmap, Figure 2. **Form:** Trajectory. **Role:** Behavior specification.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2210.14215) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

## Multimodal context

4 references.

<a id="ref-25"></a>
### External [25] WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** H. Su, Z. Liu, X. Jin, H. Dou, C. Hu, B. Li, Z. Liu, R. Xu, J. Fang, X. Zhang, Z. Yang, X. Yang, C. Gao, J. Yan, Y. Li, and W. Wu. WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory, 2026. URL https://arxiv.org/abs/2607.18840.

**Our manuscript [55]:** roadmap, Figure 2. **Form:** Multimodal. **Role:** Not assigned in roadmap.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.18840) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-94"></a>
### External [94] In-context robot learning with vlm agents (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** D. Cheng, T. Yi, Y. Fang, X. Zhang, F. Feng, Y. Li, G. Zhuang, R. Wang, S. Yang, W. Song, W. Xue, M. Wu, J. Gui, J. Wang, and T. Wu. In-context robot learning with vlm agents, 2026. URL https://arxiv.org/abs/2609.19138. GPT-Policy; first submitted 16 September 2026.

**Our manuscript [11]:** roadmap, Figure 2. **Form:** Multimodal. **Role:** Not assigned in roadmap.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.19138) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-281"></a>
### External [281] π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** Physical Intelligence et al. π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities, 2026. URL https://arxiv.org/abs/2604.15483.

**Our manuscript [6]:** roadmap, Figure 2. **Form:** Multimodal. **Role:** Task specification.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.15483) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="vima-2022"></a>
### External [100] VIMA: General Robot Manipulation with Multimodal Prompts (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** Y. Jiang, A. Gupta, Z. Zhang, G. Wang, Y. Dou, Y. Chen, et al. VIMA: General Robot Manipulation with Multimodal Prompts. arXiv preprint arXiv:2210.03094, 2022. URL https://arxiv.org/abs/2210.03094.

**Our manuscript [54]:** roadmap, Figure 2. **Form:** Multimodal. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2210.03094) — transcribed from the external survey.

**Reading-note evidence:** [p. 13](https://arxiv.org/pdf/2609.36012v1#page=13), [p. 59](https://arxiv.org/pdf/2609.36012v1#page=59), [p. 63](https://arxiv.org/pdf/2609.36012v1#page=63).

- **Deployment context:** multimodal task prompts carrying goal and procedural information
- **Action mechanism:** a context-conditioned policy uses multimodal task specifications for action inference
- **Deployment weights:** not detailed in the cited survey passages
- **Setting discussed:** task and object-combination generalization discussed in the survey
- **Survey evidence:** The survey distinguishes new object combinations from new task templates when interpreting VIMA generalization.
- **Why read it:** Illustrates how prompt content and the type of held-out task relation affect a transfer claim.
- **Adaptation target:** task specification and held-out relations
- **Evidence description:** generalization discussion in survey
- **Interpretation limit:** A new object combination and a new task template test different generalization; prompt conditioning alone does not establish learning a new relation.

## Broader domains and evaluation

6 references.

<a id="ref-101"></a>
### External [101] The Imitator Game: Benchmarking Robot Imitative Ability Beyond Action Prediction (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** X. Zhou, Y. Cai, F. Wang, R. Ju, H. Ren, R. Liu, et al. The Imitator Game: Benchmarking Robot Imitative Ability Beyond Action Prediction. arXiv preprint arXiv:2608.22301, 2026. URL https://arxiv.org/abs/2608.22301.

**Our manuscript [56]:** roadmap, Figure 2. **Form:** Not assigned in roadmap. **Role:** Task specification.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.22301) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-40"></a>
### External [40] LocoFormer: Generalist Locomotion via Long-context Adaptation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** M. Liu, D. Pathak, and A. Agarwal. LocoFormer: Generalist Locomotion via Long-context Adaptation. arXiv preprint arXiv:2509.23745, 2025. URL https://arxiv.org/abs/2509.23745.

**Our manuscript [64]:** roadmap, Figure 2. **Form:** Not assigned in roadmap. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2509.23745) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-230"></a>
### External [230] Robotwin 2.0: A scalable data generator and benchmark with strong domain randomization for robust bimanual robotic manipulation (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** T. Chen, Z. Chen, B. Chen, Z. Cai, Y. Liu, Z. Li, et al. Robotwin 2.0: A scalable data generator and benchmark with strong domain randomization for robust bimanual robotic manipulation, 2025. URL https://arxiv.org/abs/2506.18088.

**Our manuscript [71]:** roadmap, Figure 2. **Form:** Not assigned in roadmap. **Role:** Not assigned in roadmap.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2506.18088) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="relic-2024"></a>
### External [203] ReLIC: A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** A. Elawady, G. Chhablani, R. Ramrakhya, K. Yadav, D. Batra, Z. Kira, and A. Szot. ReLIC: A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI, 2024. URL https://arxiv.org/abs/2410.02751.

**Our manuscript [66]:** roadmap, Figure 2. **Form:** Not assigned in roadmap. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2410.02751) — transcribed from the external survey.

**Reading-note evidence:** [p. 33](https://arxiv.org/pdf/2609.36012v1#page=33), [p. 42](https://arxiv.org/pdf/2609.36012v1#page=42), [p. 57](https://arxiv.org/pdf/2609.36012v1#page=57), [p. 64](https://arxiv.org/pdf/2609.36012v1#page=64), [p. 73](https://arxiv.org/pdf/2609.36012v1#page=73).

- **Deployment context:** multi-episode visual experience accumulated within one unfamiliar home
- **Action mechanism:** cross-episode attention uses retained spatial experience for later navigation goals
- **Deployment weights:** frozen
- **Setting discussed:** navigation with changing starts and goals in one home
- **Survey evidence:** The survey discusses cross-episode attention as a test of within-environment experience reuse, including locating objects in an unfamiliar home.
- **Why read it:** Separates reusable local spatial knowledge from a particular route or goal.
- **Adaptation target:** environment-specific spatial knowledge
- **Evidence description:** navigation comparison in survey
- **Context amount:** up to 64k interaction steps (paper title)
- **Interpretation limit:** A remembered location is tied to a layout; transfer requires identifying which spatial facts remain valid when the environment changes.

<a id="amago-2023"></a>
### External [202] AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents (2023)

**Date basis:** Appendix A first public year; bibliography publication: 2024. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** J. Grigsby, L. Fan, and Y. Zhu. AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents. In International Conference on Learning Representations, 2024. URL https://arxiv.org/abs/2310.09971.

**Our manuscript [65]:** roadmap, Figure 2. **Form:** Not assigned in roadmap. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2310.09971) — transcribed from the external survey.

**Reading-note evidence:** [p. 33](https://arxiv.org/pdf/2609.36012v1#page=33), [p. 65](https://arxiv.org/pdf/2609.36012v1#page=65).

- **Deployment context:** trial history and feedback retained across episodes
- **Action mechanism:** an in-context reinforcement-learning policy uses retained experience to infer the task
- **Deployment weights:** frozen
- **Setting discussed:** MetaWorld ML-1 analysis discussed in the survey
- **Survey evidence:** The survey reports that short histories can identify hidden goals in the cited MetaWorld setting, while longer contexts can reduce sample efficiency.
- **Why read it:** Demonstrates that useful history length depends on the unknown information rather than context capacity alone.
- **Adaptation target:** hidden task goal
- **Evidence description:** simulation analysis
- **Interpretation limit:** The short-history result is specific to the cited MetaWorld setting.

<a id="ref-39"></a>
### External [39] RMA: Rapid Motor Adaptation for Legged Robots (2021)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** A. Kumar, Z. Fu, D. Pathak, and J. Malik. RMA: Rapid Motor Adaptation for Legged Robots. arXiv preprint arXiv:2107.04034, 2021. URL https://arxiv.org/abs/2107.04034.

**Our manuscript [57]:** roadmap, Figure 2. **Form:** Not assigned in roadmap. **Role:** Not assigned in roadmap.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2107.04034) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

## Framework mapping pending

374 references.

<a id="ref-11"></a>
### External [11] WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** Y. Feng, B. Han, J. Lyu, K. Liu, Y. Zheng, Y. Wan, W. Liu, S. Han, R. Li, Y. Zhang, F. Liu, X. Shi, L. Liu, Y. Wang, Z. Zhang, and H. Wang. WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time, 2026. URL https://arxiv.org/abs/2607.06988.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.06988) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ici-vla-2026"></a>
### External [18] ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** S. Yang, Z. Liu, X. Li, R. Xiao, K. Zhu, and M. Li. ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models, 2026. URL https://arxiv.org/abs/2609.07581. Version 1, accessed 11 September 2026.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.07581) — transcribed from the external survey.

**Reading-note evidence:** [p. 19](https://arxiv.org/pdf/2609.36012v1#page=19).

- **Deployment context:** phase-aligned micro-demonstrations retrieved for observable query inputs
- **Action mechanism:** a retriever trained with dynamic-time-warping supervision selects examples for the deployed action generator
- **Deployment weights:** not detailed in the cited survey passage
- **Setting discussed:** phase selection for vision-language-action inference
- **Survey evidence:** The survey describes phase-aligned retrieval and target-action masking during training to reduce reliance on exact action-prefix continuation.
- **Why read it:** Separates selecting the relevant execution phase from generating the action block.
- **Adaptation target:** demonstration phase and task execution
- **Evidence description:** method discussion in survey
- **Interpretation limit:** The survey describes the retrieval and training interface; detailed benchmark protocols and physical evaluation counts require the primary paper.

<a id="ref-22"></a>
### External [22] Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** J. He, G. Li, J. Zhang, C. Hou, Z. Che, and S. Zhang. Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation, 2026. URL https://arxiv.org/abs/2605.20811.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.20811) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-31"></a>
### External [31] Show-Harness: Just a VLM Agent Can Play Robots (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** Y. Chen, Z. Bai, Z. Cao, W. Zeng, K. Q. Lin, Y. Lin, G. Liang, K. Y. Ma, Q. Huang, and M. Z. Shou. Show-Harness: Just a VLM Agent Can Play Robots, 2026. URL https://arxiv.org/abs/2609.10522v1.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.10522v1) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-38"></a>
### External [38] SemAnCorr: Semantic Anchored Correspondence for Zero-Shot Manipulation Skill Transfer (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** X. Dong, W. Baron, H. Chen, U. Yoo, J. Ichnowski, and W. Zhi. SemAnCorr: Semantic Anchored Correspondence for Zero-Shot Manipulation Skill Transfer, 2026. URL https://arxiv.org/abs/2607.28382.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.28382) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-44"></a>
### External [44] MEM: Multi-Scale Embodied Memory for Vision Language Action Models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** M. Torne, K. Pertsch, H. Walke, K. Vedder, S. Nair, B. Ichter, A. Z. Ren, H. Wang, J. Tang, K. Stachowicz, K. Dhabalia, M. Equi, Q. Vuong, J. T. Springenberg, S. Levine, C. Finn, and D. Driess. MEM: Multi-Scale Embodied Memory for Vision Language Action Models. arXiv preprint arXiv:2603.03596, 2026. URL https://arxiv.org/abs/2603.03596.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.03596) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-45"></a>
### External [45] SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** C. Yin, W. Xu, J. Yang, S. Tam, H. Liu, Y. Yao, X. Zeng, J. Cui, Y. Wang, Z. Yin, and Y. Lin. SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models, 2026. URL https://arxiv.org/abs/2609.05533. Version 1, accessed 11 September 2026.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.05533) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-47"></a>
### External [47] ASPIRE: Agentic /Skills Discovery for Robotics (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** R. Lu, Y. Wu, E. Kou, L. Fu, W. Xiao, A. Mandlekar, Y. Xu, G. Shi, K. Goldberg, A. Chen, M. Chowdhury, Y. Zhu, L. J. Fan, and G. Wang. ASPIRE: Agentic /Skills Discovery for Robotics, 2026. URL https://arxiv.org/abs/2607.00272.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.00272) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-48"></a>
### External [48] A Few Words Go a Long Way: Language Guided Robot Policy Synthesis (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** D. Chen, A. R. Jain, E. Goossen, E. Romig, M. Murray, N. Walker, and M. Cakmak. A Few Words Go a Long Way: Language Guided Robot Policy Synthesis, 2026. URL https://arxiv.org/abs/2607.23784.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.23784) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-49"></a>
### External [49] Self-Evolving Embodied Agents via Skill-Harness Evolution (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** P. Wang, Z. Ma, Y. Chang, X. Luo, Y. Zhang, Z. Wang, X. Yang, S. Feng, Y. Yang, and D. Li. Self-Evolving Embodied Agents via Skill-Harness Evolution, 2026. URL https://arxiv.org/abs/2608.11350.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.11350) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-52"></a>
### External [52] Playful Agentic Robot Learning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** J. Zhang, J. Ge, H. Yoo, L. Fu, Z. Yang, Y. Liu, et al. Playful Agentic Robot Learning. arXiv preprint arXiv:2606.19419, 2026. URL https://arxiv.org/abs/2606.19419.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.19419) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-53"></a>
### External [53] Teach and Grow: An Agent-Centered Architecture for General Robot Learning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** C. Nie, Z. Liu, and H. Wang. Teach and Grow: An Agent-Centered Architecture for General Robot Learning. arXiv preprint arXiv:2608.17209, 2026. URL https://arxiv.org/abs/2608.17209.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.17209) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-55"></a>
### External [55] ContextFlow: In-Context Flow Matching for Robot Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** J. Ding, X. Dai, R. Herzig, N. Hroub, J. Mai, D. Dai, B. Ghanem, and M. Elhoseiny. ContextFlow: In-Context Flow Matching for Robot Manipulation, 2026. URL https://arxiv.org/abs/2609.06852v1.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.06852v1) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-66"></a>
### External [66] YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** T. Ohkawa, J. Arima, Y. Noguchi, M. Tateno, M. Sugiura, T. Okubo, K. Ikeuchi, Y. Shin, H. Nishizawa, N. Kanazawa, Y. Wakayama, D. Fukunaga, K. Makihara, T. Motoda, F. Erich, Y. Domae, T. Matsushima, Y. Okumatsu, and K. Ota. YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale, 2026. URL https://arxiv.org/abs/2606.10244.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.10244) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-67"></a>
### External [67] EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** R. Zheng, D. Niu, Y. Xie, J. Wang, M. Xu, Y. Jiang, F. Castañeda, F. Hu, Y. L. Tan, L. Fu, T. Darrell, F. Huang, Y. Zhu, D. Xu, and L. Fan. EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data, 2026. URL https://arxiv.org/abs/2602.16710.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2602.16710) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="zeva-2026"></a>
### External [88] Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** F. Chen, X. Ding, B. Huang, X. Li, M. Wang, J. He, et al. Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation. arXiv preprint arXiv:2608.30880, 2026. URL https://arxiv.org/abs/2608.30880.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.30880) — transcribed from the external survey.

**Reading-note evidence:** [p. 32](https://arxiv.org/pdf/2609.36012v1#page=32), [p. 54](https://arxiv.org/pdf/2609.36012v1#page=54), [p. 59](https://arxiv.org/pdf/2609.36012v1#page=59), [p. 65](https://arxiv.org/pdf/2609.36012v1#page=65), [p. 66](https://arxiv.org/pdf/2609.36012v1#page=66).

- **Deployment context:** action–effect history retained at two timescales and reused across attempts
- **Action mechanism:** a fixed policy uses retained action effects to guide subsequent control
- **Deployment weights:** frozen
- **Setting discussed:** five real tasks in the persistent-memory comparison reported in Table 16
- **Survey evidence:** The survey reports a 10–20 percentage-point success gain from enabling persistent memory on five real tasks, with a brief trace retained.
- **Why read it:** Connects cross-attempt experience reuse to a controlled memory intervention.
- **Adaptation target:** physical response across attempts
- **Evidence description:** physical robot comparison
- **Interpretation limit:** Access to prior experience and cumulative success over retries are different quantities; this comparison does not establish an improved learning rule.

<a id="ref-89"></a>
### External [89] ENPIRE: Agentic Robot Policy Self-Improvement in the Real World (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** W. Xiao, J. Xie, T. Zhang, H. Lin, L. Fu, H. Xue, J. Lu, Y. Yang, C. Dai, Z. Wang, J. Wu, G. Wang, S. S. Sastry, K. Goldberg, L. Fan, Y. Zhu, and G. Shi. ENPIRE: Agentic Robot Policy Self-Improvement in the Real World, 2026. URL https://arxiv.org/abs/2606.19980v1.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.19980v1) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-90"></a>
### External [90] Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** X. Ding, L. Mi, M. Huang, Z. Wang, C. Zhang, Z. Hao, et al. Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence. arXiv preprint arXiv:2608.16590, 2026. URL https://arxiv.org/abs/2608.16590.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.16590) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="bicicle-2026"></a>
### External [92] Bimanual Robot Manipulation via Multi-Agent In-Context Learning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** A. Palma, I. Spinelli, V. Prasad, L. Scofano, Y. Jin, G. Chalvatzaki, and F. Galasso. Bimanual Robot Manipulation via Multi-Agent In-Context Learning, 2026. URL https://arxiv.org/abs/2604.20348.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.20348) — transcribed from the external survey.

**Reading-note evidence:** [p. 18](https://arxiv.org/pdf/2609.36012v1#page=18), [p. 20](https://arxiv.org/pdf/2609.36012v1#page=20), [p. 56](https://arxiv.org/pdf/2609.36012v1#page=56).

- **Deployment context:** ten demonstrations per task in the main TWIN experiments
- **Action mechanism:** conditions one arm’s predicted trajectory on the other’s prediction, with iterative refinement and candidate selection
- **Deployment weights:** frozen
- **Setting discussed:** TWIN bimanual manipulation experiments
- **Survey evidence:** The survey reports ten demonstrations per main TWIN task and highlights added inference computation for refinement and selection.
- **Why read it:** Preserves inter-arm dependence while reducing the joint action-prediction problem.
- **Adaptation target:** coordinated bimanual behavior
- **Evidence description:** robotics benchmark
- **Context amount:** 10 demonstrations per task in main TWIN experiments
- **Interpretation limit:** Performance relies on perception, coordinate conventions, action representations, and the inference budget.

<a id="ref-95"></a>
### External [95] LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** Z. Tang, S. Chen, S. Zhang, P. Yang, Y. Liu, W. Zhao, et al. LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories. arXiv preprint arXiv:2608.18618, 2026. URL https://arxiv.org/abs/2608.18618.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.18618) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-97"></a>
### External [97] AdaTracker: Learning Adaptive In-Context Policy for Cross-Embodiment Active Visual Tracking (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** K. Wu, H. Chen, J. Han, H. Liu, C. Wang, Y. Wang, Z. Li, S. Liu, and F. Zhong. AdaTracker: Learning Adaptive In-Context Policy for Cross-Embodiment Active Visual Tracking. IEEE Robotics and Automation Letters, 2026. doi: 10.1109/LRA.2026.3692075. URL https://arxiv.org/abs/2604.20305.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.20305) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-103"></a>
### External [103] RoboMME: Benchmarking and understanding memory for robotic generalist policies (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** Y. Dai, H. Fu, J. Lee, Y. Liu, H. Zhang, J. Yang, C. Finn, N. Fazeli, and J. Chai. RoboMME: Benchmarking and understanding memory for robotic generalist policies. arXiv preprint arXiv:2603.04639, 2026. URL https://arxiv.org/abs/2603.04639.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.04639) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-104"></a>
### External [104] MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** H. Sun, H. Wang, J. Chen, W. Fang, Z. Su, J. Yi, W. Yi, H. Chen, and Z. Zhao. MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation, 2026. URL https://arxiv.org/abs/2609.07047. Version 1, accessed 11 September 2026.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.07047) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-105"></a>
### External [105] Gated Memory Policy: In-Context Memorization and Adaptation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** Y. Gao, J. J. Liu, S. Li, and S. Song. Gated Memory Policy: In-Context Memorization and Adaptation. arXiv preprint arXiv:2604.18933, 2026. URL https://arxiv.org/abs/2604.18933.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.18933) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-107"></a>
### External [107] When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** Y. Fang, Y. Feng, D. Jing, J. Liu, Y. Yang, Z. Wei, D. Szafir, and M. Ding. When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs, 2026. URL https://arxiv.org/abs/2602.17659.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2602.17659) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-108"></a>
### External [108] ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** Z. Chen, A. Tian, L. Wang, B. Joffe, Y. C. Lin, Y. Chen, S. Karamcheti, and D. Xu. ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies, 2026. URL https://arxiv.org/abs/2603.17300.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.17300) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-109"></a>
### External [109] RoboSemanticBench: Diagnosing Semantic Grounding in Action Prediction for VLA Models (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** B. Yu, Y. Zhang, H. Liu, S. Lian, Y. Wei, X. Lin, Z. Shen, C. Wu, R. Hu, B. Wang, C. Huang, and K. Chen. RoboSemanticBench: Diagnosing Semantic Grounding in Action Prediction for VLA Models, 2026. URL https://arxiv.org/abs/2606.02277.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.02277) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-110"></a>
### External [110] Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** C. Ma, L. Luo, X. Luo, X. Feng, H. Zhang, W. Liu, et al. Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks. arXiv preprint arXiv:2608.30536, 2026. URL https://arxiv.org/abs/2608.30536.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.30536) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-126"></a>
### External [126] Robot Learning from Human Videos: A Survey (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** J. Ma, E. Zhang, H. Yang, D. Li, C. Xu, G. Wang, et al. Robot Learning from Human Videos: A Survey. arXiv preprint arXiv:2604.27621, 2026. URL https://arxiv.org/abs/2604.27621.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.27621) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-127"></a>
### External [127] In-Context Reinforcement Learning under Non-Stationarity: A Survey (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** A. Run and Z. Ding. In-Context Reinforcement Learning under Non-Stationarity: A Survey, 2026. URL https://arxiv.org/abs/2607.11906.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.11906) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-128"></a>
### External [128] World Model for Robot Learning: A Comprehensive Survey (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** B. Hou, G. Li, J. Jia, T. An, X. Guo, S. Leng, H. Geng, Y. Ze, T. Harada, P. Torr, O. Mees, M. Pollefeys, Z. Liu, J. Wu, P. Abbeel, J. Malik, Y. Du, and J. Yang. World Model for Robot Learning: A Comprehensive Survey. arXiv preprint arXiv:2605.00080, 2026. URL https://arxiv.org/abs/2605.00080.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.00080) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-129"></a>
### External [129] Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** Z. Wang, B. Wang, H. Zhang, T. Du, T. Chen, G. Sun, Y. He, Z. Shen, W. Ye, and A. Li. Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines. Transactions on Machine Learning Research, 2026. URL https://arxiv.org/abs/2604.23001.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.23001) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-130"></a>
### External [130] The Embodiment Gap in Robot Foundation Models (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** Y. Domae, K. Shirai, H. Oh, R. Nakajo, T. Motoda, K. Makihara, M. Murooka, T. Yagi, Y. Bando, and R. Hanai. The Embodiment Gap in Robot Foundation Models. Transactions on Machine Learning Research, 2026. URL https://arxiv.org/abs/2608.18433.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.18433) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-133"></a>
### External [133] Demonstrate once, execute on many: Kinematic intelligence for cross-robot skill transfer (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** S. Gupta, D. H. Salunkhe, and A. Billard. Demonstrate once, execute on many: Kinematic intelligence for cross-robot skill transfer. Science Robotics, 11(113):eaea1995, 2026. doi: 10.1126/scirobotics.aea1995. URL https://doi.org/10.1126/scirobotics.aea1995.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://doi.org/10.1126/scirobotics.aea1995) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-142"></a>
### External [142] Training-Free Action Correction for VLA Model Failures via Language Feedback (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** O. Kwon, P. Ortega-Kral, A. Bucker, and J. Oh. Training-Free Action Correction for VLA Model Failures via Language Feedback. arXiv preprint arXiv:2608.29967, 2026. URL https://arxiv.org/abs/2608.29967.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.29967) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-152"></a>
### External [152] Retrieve, Don’t Retrain: Extending Vision Language Action Models to New Tasks at Test Time (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** J. Park, J. Park, T. Kim, S. Choi, D. Han, and S. Yun. Retrieve, Don’t Retrain: Extending Vision Language Action Models to New Tasks at Test Time, 2026. URL https://arxiv.org/abs/2606.15631.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.15631) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-160"></a>
### External [160] Mimic Intent, Not Just Trajectories (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** R. Huang, C. Zeng, W. Tang, J. Cai, C. Lu, and P. Cai. Mimic Intent, Not Just Trajectories. In Robotics: Science and Systems, 2026. URL https://www.roboticsproceedings.org/rss22/p206.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://www.roboticsproceedings.org/rss22/p206.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-161"></a>
### External [161] MatchingPolicy: Correspondence-Aware Policy Enables Cross-Object In-Context Learning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** Q. She, H. Yu, Z. Li, and P. Tan. MatchingPolicy: Correspondence-Aware Policy Enables Cross-Object In-Context Learning, 2026. URL https://arxiv.org/abs/2608.16715.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.16715) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-162"></a>
### External [162] In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** J. Yang, W. Huang, J. Zhang, M. Hu, and H. Guo. In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use. arXiv preprint arXiv:2608.05738, 2026. URL https://arxiv.org/abs/2608.05738.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.05738) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-166"></a>
### External [166] CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** L. Fu, J. Yu, K. El-Refai, E. Kou, H. Xue, H. Huang, et al. CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation. arXiv preprint arXiv:2603.22435, 2026. URL https://arxiv.org/abs/2603.22435.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.22435) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-175"></a>
### External [175] Sparse Meets Dense: Correspondence Guided Robotic Manipulation with Rigid-Deformable Interactions (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** Z. Zhu, Y. Chen, X. Liang, H. Bae, Y. Wang, Z. Yuan, R. Wu, and H. Dong. Sparse Meets Dense: Correspondence Guided Robotic Manipulation with Rigid-Deformable Interactions, 2026. URL https://arxiv.org/abs/2608.01083.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.01083) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-176"></a>
### External [176] VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** J. Oh, K. Kawaharazuka, and K. Okada. VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances. In IEEE/RSJ International Conference on Intelligent Robots and Systems, 2026. URL https://arxiv.org/abs/2608.05215. Accepted.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.05215) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-178"></a>
### External [178] World Action Models: The Next Frontier in Embodied AI (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84), [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** S. Wang, J. Shi, Z. Fu, X. He, F. Liu, C. Yang, Y. Zhou, Z. Fei, J. Gong, J. Fu, M. Z. Shou, X. Huang, X. Qiu, and Y.-G. Jiang. World Action Models: The Next Frontier in Embodied AI. arXiv preprint arXiv:2605.12090, 2026. URL https://arxiv.org/abs/2605.12090.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.12090) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-183"></a>
### External [183] PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** S. Choi, J. Jung, S. Kim, Y. Lee, and Y. Yu. PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control, 2026. URL https://arxiv.org/abs/2608.24115.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.24115) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-187"></a>
### External [187] PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** C.-Y. Lin, J.-W. Chen, H.-E. Chang, H.-A. Chen, S.-H. Chang, C.-P. Huang, F.-E. Yang, M.-H. Chen, Y.-T. Chen, Y.-C. F. Wang, and S.-H. Sun. PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration, 2026. URL https://arxiv.org/abs/2608.21031.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.21031) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-188"></a>
### External [188] A minimalist retargeting-guided reinforcement learning recipe for dexterous manipulation (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** Y. Feng, N. Leung, J. Wang, L. Yang, H. Qi, and P. Culbertson. A minimalist retargeting-guided reinforcement learning recipe for dexterous manipulation, 2026. URL https://arxiv.org/abs/2607.11874.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.11874) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-195"></a>
### External [195] Retrieve in Time, Correct in Frequency (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** Y. Fan, Y. Cao, P. Gao, H. Gao, G. Guo, Z. Zhang, J. Tan, B. Chen, Z. Zou, and X. Wang. Retrieve in Time, Correct in Frequency, 2026. URL https://arxiv.org/abs/2608.04527.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.04527) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-198"></a>
### External [198] ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** H. Li, F. Shen, D. Chen, L. Yang, X. Wang, J. Shi, Z. Bing, Z. Liu, and A. Knoll. ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries, 2026. URL https://arxiv.org/abs/2603.12942.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.12942) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-199"></a>
### External [199] µVLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** E. Cherepanov, N. Kachaev, D. Zelezetsky, A. Bulatov, A. Pshenitsyn, Y. Kuratov, A. Skrynnik, A. I. Panov, and A. K. Kovalev. µVLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models, 2026. URL https://arxiv.org/abs/2606.12497.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.12497) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-200"></a>
### External [200] EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** G. Yang, Z. Tu, Y. Yang, S. Mao, J. Dong, T. Chen, J. Peng, J. Xiong, J. Cao, J. Dai, W. Zhou, Y. Mu, and T. Wang. EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies, 2026. URL https://arxiv.org/abs/2606.20092.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.20092) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-204"></a>
### External [204] Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** R. Shah, Y. Li, F. Bello, Y. Zhu, and R. Martín-Martín. Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control. arXiv preprint arXiv:2606.25136, 2026. URL https://arxiv.org/abs/2606.25136.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.25136) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-205"></a>
### External [205] TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** J. Yang, Y. Lu, Y. Su, Y. Zhong, Y. Xie, Y. Zhang, et al. TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation. arXiv preprint arXiv:2608.26821, 2026. URL https://arxiv.org/abs/2608.26821.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.26821) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-206"></a>
### External [206] AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** H. Gao, Z. Ni, X. Wen, S. Xu, and R. Li. AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies. arXiv preprint arXiv:2608.29537, 2026. URL https://arxiv.org/abs/2608.29537.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.29537) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-207"></a>
### External [207] Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** Y. Zhang, H. Zhang, F. Gao, X. Li, Z. Liu, C. Zhu, J. Qiu, Y. Yan, J. Liu, W. Tang, Z. Fang, Y. Nie, C. Wei, Y. Wang, W. Ding, and C. Yu. Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents, 2026. URL https://arxiv.org/abs/2607.08448v4.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.08448v4) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-208"></a>
### External [208] Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** V. Giridhar, A. Khandelwal, J. A. Collins, I. Georgiev, and A. Garg. Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning. arXiv preprint arXiv:2608.21204, 2026. URL https://arxiv.org/abs/2608.21204.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.21204) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-209"></a>
### External [209] MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** H. Shi, W. Li, B. Xie, Y. Wang, R. Zhou, T. Wang, X. Zhang, P. Luo, and G. Huang. MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models, 2026. URL https://arxiv.org/abs/2606.09827.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.09827) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-210"></a>
### External [210] Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** W. Chen, J. S. Bhatia, C. Glossop, N. Mathihalli, R. Doshi, A. Tang, D. Driess, K. Pertsch, and S. Levine. Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control. arXiv preprint arXiv:2602.13193, 2026. URL https://arxiv.org/abs/2602.13193.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2602.13193) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-211"></a>
### External [211] Guava: An Effective and Universal Harness for Embodied Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** H. Liu, X. Li, S. Yao, P. Shi, T. Zhou, J.-B. Huang, F. Huang, and J. Mao. Guava: An Effective and Universal Harness for Embodied Manipulation, 2026. URL https://arxiv.org/abs/2606.18363.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.18363) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-212"></a>
### External [212] Addressing the Orchestration Gap in Generalist Robots via Physical Agency (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** L. Galanti, D. Shah, and T. Dao. Addressing the Orchestration Gap in Generalist Robots via Physical Agency, 2026. URL https://arxiv.org/abs/2607.21725.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.21725) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-216"></a>
### External [216] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** R. Ju, X. Wang, X. Ding, Y. Yang, H. Wu, S. Jiang, Q. Zhang, H. Wen, X. Li, W. Wang, K. Li, Y. Liu, H. Dai, W. Wang, and T. Cao. EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents, 2026. URL https://arxiv.org/abs/2605.10332.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.10332) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-217"></a>
### External [217] Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** S. Xie, Y. Zhang, R. Wang, and X. Chen. Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation, 2026. URL https://arxiv.org/abs/2603.02623.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.02623) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-218"></a>
### External [218] Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** V. Kumar. Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation, 2026. URL https://arxiv.org/abs/2603.04466.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.04466) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-219"></a>
### External [219] What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** J. Hu, M. Shridhar, C. Lu, D. Shah, H.-T. L. Chiang, J. Tan, and A. Xie. What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents, 2026. URL https://arxiv.org/abs/2606.10267.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.10267) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-220"></a>
### External [220] RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** R. Li, Y. Zhou, Y. Zhu, K. Chen, J. Wang, S. Wang, K. Hu, M. Yu, B. Jiang, Z. Su, J. Ma, X. He, Y. Shen, Y. Yang, G. Ren, M. Yao, W. Wang, and Y. Mu. RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks, 2026. URL https://arxiv.org/abs/2603.11558.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.11558) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-221"></a>
### External [221] Data Pyramid for Embodied Manipulation: A Survey (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** Y. Ye, Y. Fu, Y. Lv, B. Hou, J. Cen, L. Kong, D. Zheng, T. Chen, J. Liu, Z. Cao, Y. Lou, W. Chow, X. Sun, Y. Wang, K. Ge, X. Chi, X. Zhang, Z. Pang, Y. Zhong, S. Han, Z. Lu, W. Yuan, Q. Chen, M. Y. Wang, Y. Mu, Z. Liu, J. Yang, P. Luo, and S. Zhang. Data Pyramid for Embodied Manipulation: A Survey, 2026. URL https://arxiv.org/abs/2607.24744.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.24744) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-222"></a>
### External [222] Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** Y. Wang, P. Lin, X.-H. Chen, H. Yuan, Z. Liang, Y. Huang, A. Chen, Z. Lei, J. Zhang, T. Zhang, H. Li, T. Zhang, C. Xiao, Z. Jiao, and Q. Jin. Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data, 2026. URL https://arxiv.org/abs/2608.02580.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.02580) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-223"></a>
### External [223] HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** Simple AI, Y. Wei, J. Ma, J. Wang, W. Zhou, Y. Zuo, K. Rui, M. Li, J. Zhang, Z. Pan, X. Wang, H. Jia, H. Du, Z. Zeng, J. Ma, G. Qin, D. Zhang, and X. Li. HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone, 2026. URL https://arxiv.org/abs/2607.25895.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.25895) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-226"></a>
### External [226] Omniumi: Towards physically grounded robot learning via human-aligned multimodal interaction (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** S. Luo, Y. Li, Y. Hu, C. Yu, C. Xu, J. Zhang, G. Yao, T. Huang, R. He, and Z. Wang. Omniumi: Towards physically grounded robot learning via human-aligned multimodal interaction, 2026. URL https://arxiv.org/abs/2604.10647.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.10647) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-233"></a>
### External [233] Wall-OSS-0.5 Technical Report (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** R. Yu, P. Zhang, S. Liu, B. Liu, M. Kang, S. Li, L. Shi, E. Ma, P. Yang, C. Pan, J. Chen, D. Liu, R. Sun, M. Guo, B. Zhang, H. Zhou, Z. Xu, V. Chen, H. Huang, J. Wang, D. Kuzi, A. Zhai, H. Su, R. Gan, L. Liang, H. Wang, and Q. Wang. Wall-OSS-0.5 Technical Report, 2026. URL https://arxiv.org/abs/2605.30877v2.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.30877v2) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-238"></a>
### External [238] AgiBot World 2026 (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** AgiBot World Team. AgiBot World 2026. Official dataset documentation; accessed 13 September 2026, 2026. URL https://huggingface.co/datasets/agibot-world/AgiBotWorld2026.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-239"></a>
### External [239] AGIBOT Releases AGIBOT WORLD 2026 Theme 3 for Real-World Robot Reinforcement Learning (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** AGIBOT. AGIBOT Releases AGIBOT WORLD 2026 Theme 3 for Real-World Robot Reinforcement Learning. Official release, 1 September 2026, September 2026. URL https://agibot.com/article/231/detail/95.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://agibot.com/article/231/detail/95.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-244"></a>
### External [244] Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On-Policy Corrections (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** J. Xu, Q. Li, Y. Shen, Y. Ren, T. Davies, S. He, Z. Wang, Y. Yang, R. Cheng, and H. Dong. Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On-Policy Corrections, 2026. URL https://arxiv.org/abs/2609.03591.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.03591) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-246"></a>
### External [246] ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** H. Li, G. Zhao, Y. Liu, H. Hou, G. Ye, T. Fang, C. Liu, S. Huang, J. Liu, X. Wang, and H. Li. ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining, 2026. URL https://arxiv.org/abs/2606.17200.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.17200) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-247"></a>
### External [247] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** X. R. Team, J. Guo, P. Jin, J. Li, P. Li, Y. Li, F. Liu, W. Peng, O. Qin, Y. Su, N. Sun, Q. Sun, R. Suo, H. Wang, Y. Wang, R. Wu, C. Xia, L. Zhang, J. Zhao, G. Chen, W. Chen, X. He, B. Li, Q. Li, Z. Li, H. Qu, W. Song, D. Xiang, Y. Xie, P. Xu, H. Ye, W. Ye, H. Zhao, and Q. Zhou. Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories, 2026. URL https://arxiv.org/abs/2607.15330.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.15330) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-248"></a>
### External [248] EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** R. Punamiya, S. Kareer, Z. Liu, J. Citron, R.-Z. Qiu, X. Cai, A. Gavryushin, J. Chen, D. Liconti, L. Y. Zhu, P. Aphiwetsa, B. Li, A. Cheluva, P. Kuppili, Y. Liu, D. Patel, A. Gao, H.-Y. Chung, R. Co, R. Zbizika, J. Liu, X. Xu, H. Xiong, G. Chen, S. Oliani, W. Xuan, C. Yang, X. Wang, J. Fort, R. Newcombe, J. Gao, J. Chong, G. Matsuda, A. Doriwala, M. Pollefeys, R. Katzschmann, X. Wang, S. Song, J. Hoffman, and D. Xu. EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World, 2026. URL https://arxiv.org/abs/2604.07607.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.07607) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-249"></a>
### External [249] Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** Z. Li, B. Yang, C. Miao, K. Zhu, H. Chen, Q. Guan, Z. Wu, W. Zhan, Y. Sun, Z. Huang, Z. Shan, Z. Jin, J. Hong, T. Wang, Y. Feng, Y. Liu, Y. Wang, Y. Yang, Z. Zhou, M. Luo, H. Cheng, B. Zhang, J. Li, J. Cai, G. Yao, J. Zhang, C. Lin, R. Xu, L. Yu, C. Shen, C. Shen, and Z. Li. Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning, 2026. URL https://arxiv.org/abs/2607.14183.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.14183) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-250"></a>
### External [250] ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** Y. Cao, H. Xie, B. Wen, R. Yao, Y. Liu, Y. Huang, Z. Liao, Y. Wang, H. Liu, X. Tian, D. Su, L. Zhuo, D. Tao, X. Wang, L. Pan, and Z. Liu. ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine, 2026. URL https://arxiv.org/abs/2607.28625.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.28625) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-252"></a>
### External [252] Public summary of training content for GPT-6 Astra (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** OpenAI. Public summary of training content for GPT-6 Astra. EU AI Act training-content summary, version 1, September 2026. URL https://cdn.openai.com/pdf/gpt-6-astra-eu-ai-act-public-summary-of-training-content.pdf. Updated September 2, 2026; Section 1.3, page 2.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://cdn.openai.com/pdf/gpt-6-astra-eu-ai-act-public-summary-of-training-content.pdf) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-255"></a>
### External [255] RoboTok: An Internet-Scale Data Engine for Human Demonstration Retrieval and Dexterous Manipulation Learning (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** H. Qian, Y. Chen, Y. Xie, K. Ren, P. Chanrungmaneekul, G. Wang, B. Wen, C. Wei, and K. Hang. RoboTok: An Internet-Scale Data Engine for Human Demonstration Retrieval and Dexterous Manipulation Learning, 2026. URL https://arxiv.org/abs/2609.03199.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.03199) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-256"></a>
### External [256] SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** N. Lin, T. Ohkawa, S. Chen, R. Wen, Z. Li, L. Huang, Z. Zhu, Y. Bao, Y. Li, M. Cai, X. Ma, W. Xu, and Y. Sato. SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation, 2026. URL https://arxiv.org/abs/2608.04196.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.04196) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-258"></a>
### External [258] One-Shot Real-World Demonstration Synthesis for Scalable Bimanual Manipulation (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** H. Zhou and K. Jia. One-Shot Real-World Demonstration Synthesis for Scalable Bimanual Manipulation. In Robotics: Science and Systems, 2026. URL https://www.roboticsproceedings.org/rss22/p001.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://www.roboticsproceedings.org/rss22/p001.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-261"></a>
### External [261] SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** H. Kang, X. Ye, Y. Liu, S. H. Mantri, L. Mao, J. Fleming, et al. SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning. arXiv preprint arXiv:2605.09423, 2026. URL https://arxiv.org/abs/2605.09423.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.09423) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-262"></a>
### External [262] SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** W. Wang, Z. Li, Y. Lei, D. Martinez, X. Gao, Y. Jiang, et al. SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies. arXiv preprint arXiv:2608.31167, 2026. URL https://arxiv.org/abs/2608.31167.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.31167) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-263"></a>
### External [263] RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** S. Nasiriany, S. Nasiriany, A. Maddukuri, and Y. Zhu. RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots. arXiv preprint arXiv:2603.04356, 2026. URL https://arxiv.org/abs/2603.04356.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.04356) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-264"></a>
### External [264] PhyWorld: Physics-Faithful World Model for Video Generation (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** P. Zhao, J. Lin, T. Rupprecht, A. Akbari, C. Yang, R. Chowdhury, et al. PhyWorld: Physics-Faithful World Model for Video Generation. arXiv preprint arXiv:2605.19242, 2026. URL https://arxiv.org/abs/2605.19242.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.19242) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-265"></a>
### External [265] World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** Y. Liu, F. Feng, L. Kong, W. Lu, J. Tang, K. Zhang, et al. World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry. arXiv preprint arXiv:2604.01985, 2026. URL https://arxiv.org/abs/2604.01985.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.01985) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-270"></a>
### External [270] Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** D. Li, J. Lei, H. Wang, L. Liu, Y. Yang, Z. Wang, et al. Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis. arXiv preprint arXiv:2603.13528, 2026. URL https://arxiv.org/abs/2603.13528.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.13528) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-271"></a>
### External [271] Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** Y. Li, Z. Zhou, Y. Chen, Y. Guo, J. Liu, S. Zhang, et al. Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training. arXiv preprint arXiv:2604.21741, 2026. URL https://arxiv.org/abs/2604.21741.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.21741) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-272"></a>
### External [272] EXIMO: VLM Guided Exploration of VLA Policies (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** B. Sukhija, O. Groth, M. Shridhar, T. Hertweck, M. Bloesch, M. Wulfmeier, et al. EXIMO: VLM Guided Exploration of VLA Policies. arXiv preprint arXiv:2608.19891, 2026. URL https://arxiv.org/abs/2608.19891.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.19891) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-283"></a>
### External [283] A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** F. J. Fateh, A. S. Ali, M. Popattia, U. Nizamani, A. Konin, M. Z. Zia, and Q.-H. Tran. A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics, 2026. URL https://arxiv.org/abs/2604.15215.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.15215) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-284"></a>
### External [284] ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** Y. Hong, J. Liu, H. Yin, M. Li, L. Guibas, L. Fei-Fei, et al. ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop. arXiv preprint arXiv:2605.18746, 2026. URL https://arxiv.org/abs/2605.18746.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.18746) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-285"></a>
### External [285] Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** H. J. Lillemark, B. Huang, F. Zhan, Y. Du, and T. A. Keller. Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments. arXiv preprint arXiv:2601.01075, 2026. URL https://arxiv.org/abs/2601.01075.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2601.01075) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-286"></a>
### External [286] Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** Z. Zheng, J. Yu, X. Peng, jun shi, M. Li, C. Zhang, et al. Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation. arXiv preprint arXiv:2606.18960, 2026. URL https://arxiv.org/abs/2606.18960.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.18960) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-287"></a>
### External [287] LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** Y. Lee, H. Ju, and G. Kim. LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding. arXiv preprint arXiv:2608.19059, 2026. URL https://arxiv.org/abs/2608.19059.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.19059) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-288"></a>
### External [288] DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** M. Liao, C. Ye, J. Fei, and W. Lin. DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments. arXiv preprint arXiv:2609.00619, 2026. URL https://arxiv.org/abs/2609.00619.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.00619) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-289"></a>
### External [289] HitMem: Hierarchical Temporal 3D Memory with Multi-Modal Context-Aware Retrieval for Dynamic Environments (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** R. Tang, C. Zou, G. Wu, J. Wei, W. Chen, and J. Zhu. HitMem: Hierarchical Temporal 3D Memory with Multi-Modal Context-Aware Retrieval for Dynamic Environments. arXiv preprint arXiv:2609.00950, 2026. URL https://arxiv.org/abs/2609.00950.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.00950) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-290"></a>
### External [290] Where to Look: Can Foundation Models Reach a Target Viewpoint Through Active Exploration? (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** L. Li, M. Zhu, Z. Zhao, H. Zhao, K. Liu, L. Zhong, et al. Where to Look: Can Foundation Models Reach a Target Viewpoint Through Active Exploration? arXiv preprint arXiv:2606.01247, 2026. URL https://arxiv.org/abs/2606.01247.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.01247) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-291"></a>
### External [291] PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** V. Bhat, S. Chen, A. Zook, X. Yang, S. Birchfield, V. Blukis, et al. PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents. arXiv preprint arXiv:2608.17129, 2026. URL https://arxiv.org/abs/2608.17129.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.17129) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-292"></a>
### External [292] CR-VLA-Force: Learning Control-aware Compliance VLA Model for Robust Contact-rich Robotic Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** Z. Mai, C. Wang, C. Zeng, S. Mao, H. Zhang, S. Zhou, and C. Yang. CR-VLA-Force: Learning Control-aware Compliance VLA Model for Robust Contact-rich Robotic Manipulation, 2026. URL https://arxiv.org/abs/2609.05832v1.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.05832v1) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-296"></a>
### External [296] Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** H. Zhang, Y. Lu, B. Wang, X. Kang, Y.-L. Kuo, Z. Cheng, et al. Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents. arXiv preprint arXiv:2606.23085, 2026. URL https://arxiv.org/abs/2606.23085.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.23085) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-299"></a>
### External [299] TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90), [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** J. Zhou, B. Zhao, Y. Zhang, Y. Chen, W. Chen, Q. Li, et al. TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback. arXiv preprint arXiv:2608.25798, 2026. URL https://arxiv.org/abs/2608.25798.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.25798) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-302"></a>
### External [302] Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** Y. Zhang, D. Liu, K. Ye, C. Song, X. Li, M. Hariri, V. Singh, Y. Yin, and V. Chaudhary. Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models, 2026. URL https://arxiv.org/abs/2608.14822.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.14822) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-303"></a>
### External [303] From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** S. Xu, R. Jin, H. Zhou, B. Yue, G. Qiao, Y. Tai, et al. From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation. arXiv preprint arXiv:2605.11951, 2026. URL https://arxiv.org/abs/2605.11951.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.11951) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-304"></a>
### External [304] VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** S. Chen, H. Hadfield, A. Zook, M. A. Uy, C. H. Song, E. Coumans, X. Yang, F. Ladhak, Q. Qu, S. Birchfield, J. Tremblay, and V. Blukis. VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation, 2026. URL https://arxiv.org/abs/2606.07723.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.07723) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-306"></a>
### External [306] SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** B. Jing, M. Wang, R. Hao, C. Ge, H. Shen, J. He, et al. SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation. arXiv preprint arXiv:2608.18701, 2026. URL https://arxiv.org/abs/2608.18701.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.18701) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-307"></a>
### External [307] When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** Z. Zhu, L. Guo, Y. Mei, B. Pang, Z. Zhang, X. He, et al. When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution. arXiv preprint arXiv:2605.14504, 2026. URL https://arxiv.org/abs/2605.14504.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.14504) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-308"></a>
### External [308] PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** Y. Zhan, B. He, Z. Tang, and C. Xiao. PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments. arXiv preprint arXiv:2608.14441, 2026. URL https://arxiv.org/abs/2608.14441.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.14441) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-309"></a>
### External [309] What Are We Actually Benchmarking in Robot Manipulation? (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** T. Jiang, X. Tan, S. Wheeler, L. Sun, T. W. Ayalew, and M. Walter. What Are We Actually Benchmarking in Robot Manipulation?, 2026. URL https://arxiv.org/abs/2606.04233.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.04233) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-312"></a>
### External [312] Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** W. Gu, A. Gupta, A. Sah, R. Varghese, L. S. Vanam, P. Adireddi, P. Karkus, and N. Gopalan. Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation, 2026. URL https://arxiv.org/abs/2609.08209. Version 1, accessed 11 September 2026.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.08209) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-314"></a>
### External [314] H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** D. Rong, Y. Shi, C. Ma, J. Cao, Z. Wang, Z. Zhang, et al. H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models. arXiv preprint arXiv:2608.13049, 2026. URL https://arxiv.org/abs/2608.13049.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.13049) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-316"></a>
### External [316] $τ\_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** X. Cai, Y. Cai, B. Chen, J. Chen, Z. Chen, S. Feng, et al. $τ\_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation. arXiv preprint arXiv:2608.16885, 2026. URL https://arxiv.org/abs/2608.16885.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.16885) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-317"></a>
### External [317] SAIL: Test-Time Scaling for In-Context Imitation Learning with VLM (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** M. Sato, Y. Iwasawa, Y. Tang, and S. Kuroki. SAIL: Test-Time Scaling for In-Context Imitation Learning with VLM. arXiv preprint arXiv:2603.08269, 2026. URL https://arxiv.org/abs/2603.08269.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.08269) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-325"></a>
### External [325] Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** C.-P. Huang, Y. Man, Z. Yu, M.-H. Chen, J. Kautz, Y.-C. F. Wang, and F.-E. Yang. Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning, 2026. URL https://arxiv.org/abs/2601.09708v2.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2601.09708v2) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-326"></a>
### External [326] The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** Y. Duan, Y. Liu, Z. Tang, H. Chen, J. Zhou, Y. Liu, B. Xu, Y. Wu, S. Chen, Y. Zhou, H. Wang, X. Yu, S. Han, X. Zhu, L. Zhou, B. Lu, W. Zhou, J. Liu, N. Fang, J. Tian, R. Chen, Y. Li, K. Zuo, K. Zhang, J. Qiu, C. He, G. Li, B. Zhou, Z. Liu, Z. Wen, J. Kang, X. Zhou, and F. Wu. The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement, 2026. URL https://arxiv.org/abs/2609.11873v1.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.11873v1) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-328"></a>
### External [328] VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** Y. Guo, T. Lee, L. X. Shi, J. Chen, P. Liang, and C. Finn. VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model. arXiv preprint arXiv:2602.12063, 2026. URL https://arxiv.org/abs/2602.12063.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2602.12063) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-329"></a>
### External [329] World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** X. Liu, Z. Bai, H. Ci, K. Y. Ma, and M. Z. Shou. World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy. arXiv preprint arXiv:2602.06508, 2026. URL https://arxiv.org/abs/2602.06508.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2602.06508) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-330"></a>
### External [330] Motus2: A Self-Evolving General World Model for Dexterous Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** H. Bi, Z. Zhou, Y. Tang, J. Pang, S. Huang, H. Liu, R. Wang, S. Huang, Y. Wang, Y. Cheng, R. Zhao, Z. Li, H. Tan, X. Liu, J. Wan, J. Liu, M. Zhao, F. Bao, and J. Zhu. Motus2: A Self-Evolving General World Model for Dexterous Manipulation, 2026. URL https://arxiv.org/abs/2608.30237.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.30237) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-335"></a>
### External [335] TADreamer: Zero-Shot Language-Guided 3D Navigation for Terrestrial-Aerial Bimodal Robots via Video Imagination (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** X. Li, T. Lai, X. Huang, R. Pang, S. Shen, J. Chen, Z. Pan, C. Xu, F. Gao, and Y. Cao. TADreamer: Zero-Shot Language-Guided 3D Navigation for Terrestrial-Aerial Bimodal Robots via Video Imagination. arXiv preprint arXiv:2609.19824, 2026. URL https://arxiv.org/abs/2609.19824.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.19824) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-336"></a>
### External [336] GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** R. Wang, H.-L. Hsu, S. Mehta, J. Kim, Z. Dou, and M. Pajic. GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning. arXiv preprint arXiv:2609.19315, 2026. URL https://arxiv.org/abs/2609.19315.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.19315) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-337"></a>
### External [337] StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** J. Huang, Y. Hu, Z. Li, R. Qi, Y. Xiao, Y. Wu, T. Ba, Z. Zhang, and Y. Zhang. StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation. arXiv preprint arXiv:2609.20791, 2026. URL https://arxiv.org/abs/2609.20791.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.20791) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-338"></a>
### External [338] Navi-Agent: Unlocalized Monocular Navigation Agent (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** W. Xie, M. Hong, Y. Wang, Y. Ji, Y. Zhou, S. Wu, S. Sirejiding, H. Zhou, Y.-C. Chen, M. Ling, Y. Ding, and H. Lu. Navi-Agent: Unlocalized Monocular Navigation Agent. arXiv preprint arXiv:2609.20388, 2026. URL https://arxiv.org/abs/2609.20388.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.20388) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-339"></a>
### External [339] LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** W. Li, Y. Chen, W. Li, and Q. Wu. LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation. arXiv preprint arXiv:2609.19796, 2026. URL https://arxiv.org/abs/2609.19796.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.19796) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-340"></a>
### External [340] SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** K. Agrawal, M. A. Rahman, R. A. Yeh, and Z. Kingston. SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation. arXiv preprint arXiv:2609.20648, 2026. URL https://arxiv.org/abs/2609.20648.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.20648) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-341"></a>
### External [341] Learning and Transferring Closed-Loop Robot Software (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** S. Kuroki and Y. Tang. Learning and Transferring Closed-Loop Robot Software. arXiv preprint arXiv:2609.19906, 2026. URL https://arxiv.org/abs/2609.19906.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.19906) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-342"></a>
### External [342] HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** Z. Han, Y. Zeng, J. Zhang, Z. Zhao, Y. Wang, Y. Jin, S. Li, S. Chen, W. Huang, R. Li, H. Shen, and H. Dong. HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface. arXiv preprint arXiv:2609.20659, 2026. URL https://arxiv.org/abs/2609.20659.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.20659) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-343"></a>
### External [343] CoreSense: Traceable Failure Recall and Conflict-Aware Belief Gating for Auditable Robot Decisions (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** Z. Li. CoreSense: Traceable Failure Recall and Conflict-Aware Belief Gating for Auditable Robot Decisions. arXiv preprint arXiv:2609.19512, 2026. URL https://arxiv.org/abs/2609.19512.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.19512) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-344"></a>
### External [344] VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** Z. Zhang, J. Jin, Y. Wang, Z. Zhang, H. Diao, L. Wang, and H. Lu. VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control. arXiv preprint arXiv:2609.19554, 2026. URL https://arxiv.org/abs/2609.19554.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.19554) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-345"></a>
### External [345] REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** H. Liu, Q. Li, Y. Ding, J. Wen, K. Ren, Y. Ma, T. Jian, Z. Wang, Z. Yu, X. Li, and Z. Song. REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention. arXiv preprint arXiv:2609.14633, 2026. URL https://arxiv.org/abs/2609.14633.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.14633) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-347"></a>
### External [347] One-Shot Cross-Geometry Skill Transfer through Part Decomposition (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** S. Thompson, O. Biza, and G. Konidaris. One-Shot Cross-Geometry Skill Transfer through Part Decomposition, 2026. URL https://arxiv.org/abs/2604.15455.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2604.15455) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-348"></a>
### External [348] RoboRSI: Stable, Efficient, and Reusable Robot Self-Evolution in Complex Real-World Environments (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** Noematrix Team. RoboRSI: Stable, Efficient, and Reusable Robot Self-Evolution in Complex Real-World Environments. Research Blog, September 2026. URL https://lab.noematrix.ai/blog/2-roborsi/.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://lab.noematrix.ai/blog/2-roborsi/) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-349"></a>
### External [349] ETA: A New Agentic Paradigm for Embodied Tasks (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** Y. Chen, Z. Huai, S. Li, Y. Wang, H. Zhang, Y. Zhang, H. Chen, J. Gong, Y.-G. Jiang, and X. Qiu. ETA: A New Agentic Paradigm for Embodied Tasks, 2026. URL https://arxiv.org/abs/2608.03924.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.03924) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-350"></a>
### External [350] RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** J. Huang, Y. Hu, Z. Li, R. Qi, Y. Xiao, Z. Zhang, M. Coates, T. Cao, and Y. Zhang. RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning, 2026. URL https://arxiv.org/abs/2607.18060.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.18060) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-361"></a>
### External [361] CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** H. Li, X. Dong, H. Jiang, Y. Zhou, and X. Ma. CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval, 2026. URL https://arxiv.org/abs/2603.07997.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2603.07997) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-362"></a>
### External [362] HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** A. Liu, B. Liu, H. Ding, Y. Jiang, Y. Chen, F. Tang, C. Leng, H. Zhang, and J. Cheng. HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation, 2026. URL https://arxiv.org/abs/2607.29600.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2607.29600) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-363"></a>
### External [363] Zeva-Ego: Egocentric Mid-Training with In-Context Causal Learning for Robot Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** B. Huang, X. Ding, F. Chen, K. Li, W. Sun, H. Wu, Y. Liu, and T. Cao. Zeva-Ego: Egocentric Mid-Training with In-Context Causal Learning for Robot Manipulation, 2026. URL https://arxiv.org/abs/2609.24411.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.24411) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-364"></a>
### External [364] RopeFormer: Cross-Trial Adaptation from Interaction History for Dynamic Rope Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** M. Wu, K. Yao, S. Luan, M. Tomizuka, and Y. Chen. RopeFormer: Cross-Trial Adaptation from Interaction History for Dynamic Rope Manipulation, 2026. URL https://arxiv.org/abs/2609.23432.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.23432) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-365"></a>
### External [365] Transferring the Intelligence of VLMs to Robotic Control (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** M.-H. Guo, Z.-H. Mo, J.-J. Wang, Y. Zhang, K. Wang, Y.-X. Deng, J.-P. Zhang, Y. Rao, and S.-M. Hu. Transferring the Intelligence of VLMs to Robotic Control, 2026. URL https://arxiv.org/abs/2609.22966.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.22966) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-366"></a>
### External [366] H2RBench: A Real-to-Sim Benchmark for Evaluating Human-to-Robot Transfer (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** C. Xiao, H. Zhan, S. Krishna, P. Meng, M. Z. Irshad, S. Zakharov, and D. Held. H2RBench: A Real-to-Sim Benchmark for Evaluating Human-to-Robot Transfer, 2026. URL https://arxiv.org/abs/2609.24778.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.24778) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-367"></a>
### External [367] Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** K. Soni, A. Sehgal, V. Dave, and E. Rueckert. Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models, 2026. URL https://arxiv.org/abs/2609.21740.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.21740) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-368"></a>
### External [368] MetaPusher: Meta Learning and Planning for Nonprehensile Manipulation of Unseen Objects with Rapid Online Adaption (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** D. Lee, S. Golestaneh, J. Singh, Z. Zhong, A. Kapoutsis, and C. Chamzas. MetaPusher: Meta Learning and Planning for Nonprehensile Manipulation of Unseen Objects with Rapid Online Adaption, 2026. URL https://arxiv.org/abs/2609.21122.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.21122) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-369"></a>
### External [369] KnowDemo: Knowledge-Guided Robot Demonstration Generation from Human Videos (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** Z. Gao, Y. Zhan, M. Khoshnazar, J. Schäfer, and M. Beetz. KnowDemo: Knowledge-Guided Robot Demonstration Generation from Human Videos, 2026. URL https://arxiv.org/abs/2609.21229.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.21229) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-370"></a>
### External [370] Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** G. Jena, K. Wanaskar, V. Jain, A. Chadha, V. Sharma, and A. Das. Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills, 2026. URL https://arxiv.org/abs/2608.01851.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.01851) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-371"></a>
### External [371] World-action models for robot learning and control: A survey (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** Z. Lu, H. Zhai, G. Wang, H. Zeng, J. Yang, J. Liu, L. Cheng, Y. Zhang, Y. Qiu, Z. Cheng, I. Laptev, D. Xu, B. Riviere, G. Loianno, E. Xing, and X. Zuo. World-action models for robot learning and control: A survey, 2026. URL https://arxiv.org/abs/2609.16074.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.16074) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-372"></a>
### External [372] In-Context Learning from Demonstrations for Robotic Manipulation: A Survey (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** W. Li. In-Context Learning from Demonstrations for Robotic Manipulation: A Survey. Preprints.org, manuscript 202609.0780, version 1, September 2026. URL https://www.preprints.org/manuscript/202609.0780.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://www.preprints.org/manuscript/202609.0780) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-374"></a>
### External [374] EvoEmpirBench: Dynamic Spatial Reasoning with Agent-ExpVer (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** P. Zhao, L. Wang, M. Wang, C. Chen, F. Zhou, and H. Huang. EvoEmpirBench: Dynamic Spatial Reasoning with Agent-ExpVer. Proceedings of the AAAI Conference on Artificial Intelligence, 40(43):36564–36572, 2026. doi: 10.1609/aaai.v40i43.40979. URL https://ojs.aaai.org/index.php/AAAI/article/view/40979.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://ojs.aaai.org/index.php/AAAI/article/view/40979) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-375"></a>
### External [375] WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** Y. Zhang, J. Su, H. Huang, Y. Chang, T. Zhou, X. Xu, Y. Xu, Y. Li, Z. Li, and Y.-C. Chen. WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents. arXiv preprint arXiv:2606.18847, 2026. URL https://arxiv.org/abs/2606.18847.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.18847) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-376"></a>
### External [376] Affordance Agent Harness: Verification-Gated Skill Orchestration (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** H. Huang, J. Shi, Y. Li, and Y. Chen. Affordance Agent Harness: Verification-Gated Skill Orchestration. arXiv preprint arXiv:2605.00663, 2026. URL https://arxiv.org/abs/2605.00663.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2605.00663) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-377"></a>
### External [377] RoboStressBench: Benchmarking VLM Robustness to Physical Visual Stress in Embodied Scenes (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** L. Wu, Y. Zhao, J. Zhang, S. Chen, W. Chen, Z. Chen, T. Xu, Q. He, H. Hu, H. Huang, Y. Wei, W. Li, Y. Li, and Y.-C. Chen. RoboStressBench: Benchmarking VLM Robustness to Physical Visual Stress in Embodied Scenes. arXiv preprint arXiv:2606.00828, 2026. URL https://arxiv.org/abs/2606.00828.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.00828) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-378"></a>
### External [378] No Place to Hide: Benchmarking Video Hallucination with Background-Controlled Pairs (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** H. Huang, H. H. Chen, M. Luo, J. Du, S. Xu, Z. Chen, Y. Huang, Y. Li, and Y.-C. Chen. No Place to Hide: Benchmarking Video Hallucination with Background-Controlled Pairs. arXiv preprint arXiv:2606.31933, 2026. URL https://arxiv.org/abs/2606.31933.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2606.31933) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-379"></a>
### External [379] Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** Z. Li, Y. Zhang, W. Li, H. Huang, C. Wang, S. Deng, Y. Wei, T. Zhang, B. Xie, B. Zhou, Y. Chang, K. Zhou, Y.-C. Chen, J. Cheng, and Y. Li. Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation, 2026. URL https://arxiv.org/abs/2609.29389.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.29389) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-380"></a>
### External [380] RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** Z. Li, Y. Zhang, H. Huang, B. Zhou, W. Li, C. Wang, Y. Chang, Y. Wei, T. Zhang, Y.-C. Chen, K. Zhou, Y. Li, and J. Cheng. RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning, 2026. URL https://arxiv.org/abs/2609.29394.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.29394) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-381"></a>
### External [381] MemBodied: Recurrent Associative Memory for Vision-Language-Action Models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** T. D. Pala, N. Majumder, B. Goh, R. Yee, J. Yang, L. Chen, and S. Poria. MemBodied: Recurrent Associative Memory for Vision-Language-Action Models, 2026. URL https://arxiv.org/abs/2609.28256.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.28256) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-382"></a>
### External [382] EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** H. You, Z. Shen, Y. Liu, Z. Zheng, L. Zha, K. Yamazaki, M. Zhang, S. Huang, J. Sun, Q. Chen, L. He, K. Liu, H. Chang, K. Fragkiadaki, D. Shah, M. Schwager, P. Henderson, I. Abraham, and C. Xu. EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics, 2026. URL https://arxiv.org/abs/2609.27308.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.27308) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-383"></a>
### External [383] NavProbe: Evidence-Grounded Reasoning with Active Memory Retrieval for Zero-Shot Navigation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** J. Liu, S. Yao, J. Gu, and L. Xu. NavProbe: Evidence-Grounded Reasoning with Active Memory Retrieval for Zero-Shot Navigation, 2026. URL https://arxiv.org/abs/2609.27526.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.27526) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-384"></a>
### External [384] Talk2Escape: Conversational Grounding for Vision-and-Language Navigation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** Z. Li, S. Lin, Y. Shao, J. Zhang, X. Shi, S. Li, and Q. Wu. Talk2Escape: Conversational Grounding for Vision-and-Language Navigation, 2026. URL https://arxiv.org/abs/2609.28296.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.28296) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-385"></a>
### External [385] Memory That Changes Action Is Not Memory That Guides It: Counterfactual Auditing of History-Conditioned Robot Policies (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** J. Zhang, Y. Xiang, and C. Chen. Memory That Changes Action Is Not Memory That Guides It: Counterfactual Auditing of History-Conditioned Robot Policies, 2026. URL https://arxiv.org/abs/2609.27247.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.27247) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-386"></a>
### External [386] Task-Prototype Guided Flow Matching for Few-Shot Generalization in Vision-Language Robot Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** Y. Wang, G. Zhang, and J. Wang. Task-Prototype Guided Flow Matching for Few-Shot Generalization in Vision-Language Robot Manipulation, 2026. URL https://arxiv.org/abs/2609.27780.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.27780) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-387"></a>
### External [387] Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** D. Yi, P. Sun, C. Rong, J. Wang, X. Dai, X. Yue, and X. Lin. Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams, 2026. URL https://arxiv.org/abs/2609.28429.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.28429) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-388"></a>
### External [388] World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94), [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** Y. Zhang, H. Huang, Y. Chang, J. Su, B. Zhou, Y. Xu, W. Chen, T. Zhou, C. Wang, T. Zhang, Y. Wei, W. Li, S. Deng, Y. Li, Y.-C. Chen, and Z. Li. World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal, 2026. URL https://arxiv.org/abs/2609.29964.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.29964) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-389"></a>
### External [389] GLOW: A generative learning framework for general-purpose embodied intelligence (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** Knowin AI. GLOW: A generative learning framework for general-purpose embodied intelligence. Online technical report, September 2026. URL https://knowinai.com/tech.html. Accessed September 26, 2026.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://knowinai.com/tech.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-390"></a>
### External [390] Rapid: Robot agentic programming from demonstrations (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** Y. Liu, J. Mao, D. Hsu, L. P. Kaelbling, and T. Lozano-Pérez. Rapid: Robot agentic programming from demonstrations, 2026. URL https://arxiv.org/abs/2609.30249.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30249) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-391"></a>
### External [391] Training-free behavior cloning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** M. Adang, T. Chen, L. Osterberg, A. Swann, and M. Schwager. Training-free behavior cloning, 2026. URL https://arxiv.org/abs/2609.30134.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30134) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-392"></a>
### External [392] Traceflow: Guiding frozen flow-matching robot policies with success and failure traces (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** J. Zhang, R. Liu, Y. Zhang, and Y. Yang. Traceflow: Guiding frozen flow-matching robot policies with success and failure traces, 2026. URL https://arxiv.org/abs/2609.20646.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.20646) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-393"></a>
### External [393] Self-adaptive vla for robust robot deployment (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** H. Zhang, C. Lin, T.-H. Wang, Z. Xu, and C. Gan. Self-adaptive vla for robust robot deployment, 2026. URL https://arxiv.org/abs/2609.30092.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30092) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-394"></a>
### External [394] Mimir: A neuro-symbolic memory system with dynamic grounding for embodied agents in interactive environments (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** H. Xu, Z. He, H. Wang, J. Xu, and H. Dong. Mimir: A neuro-symbolic memory system with dynamic grounding for embodied agents in interactive environments, 2026. URL https://arxiv.org/abs/2608.04933.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2608.04933) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-395"></a>
### External [395] Occ4m: Object-centric 4d memory for spatiotemporal reasoning in long-horizon manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** J. B. Jedlicki, T. Dieudonné, and H. Yang. Occ4m: Object-centric 4d memory for spatiotemporal reasoning in long-horizon manipulation, 2026. URL https://arxiv.org/abs/2609.28798.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.28798) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-396"></a>
### External [396] Sparsenav: Instruction-conditioned sparse semantic perception for training-free vision-language navigation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** Q. Chen, J. Kang, R. Lin, Z. Zhang, E. Feng, C. Zheng, X. Dong, and J. Lin. Sparsenav: Instruction-conditioned sparse semantic perception for training-free vision-language navigation, 2026. URL https://arxiv.org/abs/2609.26408.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.26408) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-397"></a>
### External [397] Workspace models: Lightweight robotic memory via saliency-driven supervision (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** N. Dashora, D. Chen, I. Shenfeld, J. Marangola, P. Agrawal, and M. Simchowitz. Workspace models: Lightweight robotic memory via saliency-driven supervision, 2026. URL https://arxiv.org/abs/2609.20820.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.20820) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-398"></a>
### External [398] Harnesspai: An evolving harness for physical ai (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** X. Wang, W. Wu, M. Zhang, Z. Wang, K. Shao, J. Luan, Y. Li, Q. Li, S. Gu, H. Zhou, S. Shi, F. Ni, S. Lu, W. Meng, K. Li, J. Wu, K. Zhao, S. Guo, G. Li, Y. Tang, Z. Zhang, Y. Xie, and H. Qu. Harnesspai: An evolving harness for physical ai, 2026. URL https://arxiv.org/abs/2609.29166.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.29166) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-399"></a>
### External [399] Robofollow: Unveiling the instruction following mirage in embodied agents (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** C. Guo, Y. Xie, B. Tan, Z. Chang, Z. Yin, Q. Ma, Y. Wang, C. Liang, and Z. Zhang. Robofollow: Unveiling the instruction following mirage in embodied agents, 2026. URL https://arxiv.org/abs/2609.25636.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.25636) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-400"></a>
### External [400] Roborecover: Benchmarking robot policy recovery under execution deviations (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** Y. Li, C. Zhao, Z. Wang, J. Wang, C. Shao, Y. Lin, H. Shen, and J. Zhang. Roborecover: Benchmarking robot policy recovery under execution deviations, 2026. URL https://arxiv.org/abs/2609.28952.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.28952) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-401"></a>
### External [401] Memory as plans: World-action modeling with memory-grounded planning (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** S. Zhao, H. Xie, W. Zhao, C. Zhang, H. Wang, C. Wang, Q. Liu, and S. Zhang. Memory as plans: World-action modeling with memory-grounded planning, 2026. URL https://arxiv.org/abs/2609.11561.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.11561) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-402"></a>
### External [402] Causal-history test-time scaling for failure recovery in autoregressive world-action models (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** L. Li, L. Chen, Kwunhang, Wong, J. Lei, S. Jin, S. Du, C. Zhang, S. Ma, W. Zhang, J. Xiao, Kwang-Ting, and Cheng. Causal-history test-time scaling for failure recovery in autoregressive world-action models, 2026. URL https://arxiv.org/abs/2609.18016.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.18016) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-403"></a>
### External [403] 2am: Grounding agent-side memory as guidance for steerable action models in long-horizon manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** Y. Hu, F. Chen, X. Cao, and R. Detry. 2am: Grounding agent-side memory as guidance for steerable action models in long-horizon manipulation, 2026. URL https://arxiv.org/abs/2609.11308.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.11308) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-404"></a>
### External [404] HIRE: History-Conditioned Interaction Reasoning and High-Rate Execution for Visually Aliased Precision Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** R. Li, W. He, C. Lu, X. Chen, and X.-Y. Zhang. HIRE: History-Conditioned Interaction Reasoning and High-Rate Execution for Visually Aliased Precision Manipulation, 2026. URL https://arxiv.org/abs/2609.30828.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30828) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-405"></a>
### External [405] POIL: Point-based One-Shot Imitation Learning with Stable Dynamical Systems (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** S. M. Kim, J. Seo, H. Heo, J. Lee, Y. Lee, and Y. M. Kim. POIL: Point-based One-Shot Imitation Learning with Stable Dynamical Systems, 2026. URL https://arxiv.org/abs/2609.30404.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30404) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-406"></a>
### External [406] Actively Resolving Contextual Uncertainty for Underspecified Tasks in Natural Language (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** Z. Ravichandran, J. Diller, F. Cladera, V. Murali, G. J. Pappas, and V. Kumar. Actively Resolving Contextual Uncertainty for Underspecified Tasks in Natural Language, 2026. URL https://arxiv.org/abs/2609.30428.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30428) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-407"></a>
### External [407] Coding Agents for Generalized Task and Motion Planning Problems (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** M. Merler, B. Li, J. Roy, Y. Liang, Q. Wang, Y. Huang, and T. Silver. Coding Agents for Generalized Task and Motion Planning Problems, 2026. URL https://arxiv.org/abs/2609.30233.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30233) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-408"></a>
### External [408] Representation-Guided Generation and Integration of Executable Programs for Robot Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** R. Yang, M. Yu, and C. Fan. Representation-Guided Generation and Integration of Executable Programs for Robot Manipulation, 2026. URL https://arxiv.org/abs/2609.31337.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.31337) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-409"></a>
### External [409] HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** S. Choi, S. Ye, N. Bui, A. Shrivastava, K. Ryu, D. Tirumala, M. Wulfmeier, and N. Mehr. HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation, 2026. URL https://arxiv.org/abs/2609.30594.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30594) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-410"></a>
### External [410] DualManip: Agentic Dynamic Manipulation via Dual-Path Semantic Reasoning and Geometric Adaptation (2026)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** C. Li, Y. Di, Y. Li, R. Zhang, M. Li, and X. Ji. DualManip: Agentic Dynamic Manipulation via Dual-Path Semantic Reasoning and Geometric Adaptation, 2026. URL https://arxiv.org/abs/2609.31112.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.31112) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-411"></a>
### External [411] PHASE: Compliance-Enabled Tactile Phase Retrieval for Few-Shot Insertion Learning (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** J. Siburian, C. C. Beltran-Hernandez, T. Matsushima, Y. Iwasawa, M. Hamaya, and M. Nishimura. PHASE: Compliance-Enabled Tactile Phase Retrieval for Few-Shot Insertion Learning, 2026. URL https://arxiv.org/abs/2609.30889.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30889) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-412"></a>
### External [412] Audit Before You Commit: Locating Belief Failures in Active Identification for One-Shot Manipulation (2026)

**Date basis:** Bibliography year. **Bibliography:** [p. 95](https://arxiv.org/pdf/2609.36012v1#page=95).

**Citation:** M. Abouagour and B.-C. Min. Audit Before You Commit: Locating Belief Failures in Active Identification for One-Shot Manipulation, 2026. URL https://arxiv.org/abs/2609.30608.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2609.30608) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-21"></a>
### External [21] OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** R. G. Goswami, P. Krishnamurthy, Y. LeCun, and F. Khorrami. OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation. arXiv preprint arXiv:2505.20425, 2025. URL https://arxiv.org/abs/2505.20425.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2505.20425) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-36"></a>
### External [36] Learning a Thousand Tasks in a Day (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** K. Dreczkowski, P. Vitiello, V. Vosylius, and E. Johns. Learning a Thousand Tasks in a Day. Science Robotics, 10:eadv7594, 2025. doi: 10.1126/scirobotics.adv7594. URL https://arxiv.org/abs/2511.10110.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2511.10110) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-37"></a>
### External [37] One-Shot Dual-Arm Imitation Learning (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** Y. Wang and E. Johns. One-Shot Dual-Arm Imitation Learning. In IEEE International Conference on Robotics and Automation, 2025. URL https://arxiv.org/abs/2503.06831.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2503.06831) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-42"></a>
### External [42] MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** H. Shi, B. Xie, Y. Liu, L. Sun, F. Liu, T. Wang, E. Zhou, H. Fan, X. Zhang, and G. Huang. MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation, 2025. URL https://arxiv.org/abs/2508.19236.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2508.19236) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-43"></a>
### External [43] MemER: Scaling Up Memory for Robot Control via Experience Retrieval (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** A. Sridhar, J. Pan, S. Sharma, and C. Finn. MemER: Scaling Up Memory for Robot Control via Experience Retrieval. arXiv preprint arXiv:2510.20328, 2025. URL https://arxiv.org/abs/2510.20328.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2510.20328) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-51"></a>
### External [51] Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** Y. Meng, Z. Sun, M. Fest, X. Li, Z. Bing, and A. Knoll. Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills. arXiv preprint arXiv:2509.18597, 2025. URL https://arxiv.org/abs/2509.18597.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2509.18597) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-60"></a>
### External [60] AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** AgiBot-World-Contributors. AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems. arXiv preprint arXiv:2503.06669, 2025. URL https://arxiv.org/abs/2503.06669.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2503.06669) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-61"></a>
### External [61] Galaxea Open-World Dataset and G0 Dual-System VLA Model (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** T. Jiang, T. Yuan, Y. Liu, C. Lu, J. Cui, X. Liu, S. Cheng, J. Gao, H. Xu, and H. Zhao. Galaxea Open-World Dataset and G0 Dual-System VLA Model, 2025. URL https://arxiv.org/abs/2509.00576.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2509.00576) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-65"></a>
### External [65] EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** R. Hoque, P. Huang, D. J. Yoon, M. Sivapurapu, and J. Zhang. EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video, 2025. URL https://arxiv.org/abs/2505.11709.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2505.11709) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-82"></a>
### External [82] Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** C. Xu, T. K. Nguyen, E. Dixon, C. Rodriguez, P. Miller, R. Lee, P. Shah, R. Ambrus, H. Nishimura, and M. Itkina. Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies. arXiv preprint arXiv:2503.08558, 2025. URL https://arxiv.org/abs/2503.08558.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2503.08558) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-93"></a>
### External [93] ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation (2025)

**Date basis:** Appendix A first public year; bibliography publication: 2026. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** Z. Chen, C. Gao, L. Shao, J. Shi, J. Huo, and Y. Gao. ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation. In AAAI Conference on Artificial Intelligence, 2026. URL https://ojs.aaai.org/index.php/AAAI/article/view/38881.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://ojs.aaai.org/index.php/AAAI/article/view/38881) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-102"></a>
### External [102] LMAct: A benchmark for in-context imitation learning with long multimodal demonstrations (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** A. Ruoss, F. Pardo, H. Chan, B. Li, V. Mnih, and T. Genewein. LMAct: A benchmark for in-context imitation learning with long multimodal demonstrations. In Proceedings of the 42nd International Conference on Machine Learning, volume 267 of Proceedings of Machine Learning Research, pages 52303–52344, 2025. URL https://proceedings.mlr.press/v267/ruoss25a.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://proceedings.mlr.press/v267/ruoss25a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-106"></a>
### External [106] LIBERO-PRO: Towards robust and fair evaluation of vision-language-action models beyond memorization (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** X. Zhou, Y. Xu, G. Tie, Y. Chen, G. Zhang, D. Chu, P. Zhou, and L. Sun. LIBERO-PRO: Towards robust and fair evaluation of vision-language-action models beyond memorization. arXiv preprint arXiv:2510.03827, 2025. URL https://arxiv.org/abs/2510.03827.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2510.03827) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-120"></a>
### External [120] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** NVIDIA, J. Bjorck, F. Castañeda, N. Cherniadev, X. Da, R. Ding, L. J. Fan, Y. Fang, D. Fox, F. Hu, S. Huang, J. Jang, Z. Jiang, J. Kautz, K. Kundalia, L. Lao, Z. Li, Z. Lin, K. Lin, G. Liu, E. Llontop, L. Magne, A. Mandlekar, A. Narayan, S. Nasiriany, S. Reed, Y. L. Tan, G. Wang, Z. Wang, J. Wang, Q. Wang, J. Xiang, Y. Xie, Y. Xu, Z. Xu, S. Ye, Z. Yu, A. Zhang, H. Zhang, Y. Zhao, R. Zheng, and Y. Zhu. GR00T N1: An Open Foundation Model for Generalist Humanoid Robots. arXiv preprint arXiv:2503.14734, 2025. URL https://arxiv.org/abs/2503.14734.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2503.14734) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-125"></a>
### External [125] A Survey of In-Context Reinforcement Learning (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** A. Moeini, J. Wang, J. Beck, E. Blaser, S. Whiteson, R. Chandra, et al. A Survey of In-Context Reinforcement Learning. arXiv preprint arXiv:2502.07978, 2025. URL https://arxiv.org/abs/2502.07978.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2502.07978) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-145"></a>
### External [145] Memory in the Age of AI Agents (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** Y. Hu, S. Liu, Y. Yue, G. Zhang, B. Liu, F. Zhu, J. Lin, H. Guo, S. Dou, Z. Xi, S. Jin, J. Tan, Y. Yin, J. Liu, Z. Zhang, Z. Sun, Y. Zhu, H. Sun, B. Peng, Z. Cheng, X. Fan, J. Guo, X. Yu, Z. Zhou, Z. Hu, J. Huo, J. Wang, Y. Niu, Y. Wang, Z. Yin, X. Hu, Y. Liao, Q. Li, K. Wang, W. Zhou, Y. Liu, D. Cheng, Q. Zhang, T. Gui, S. Pan, Y. Zhang, P. Torr, Z. Dou, J.-R. Wen, X. Huang, Y.-G. Jiang, and S. Yan. Memory in the Age of AI Agents. arXiv preprint arXiv:2512.13564, 2025. URL https://arxiv.org/abs/2512.13564.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2512.13564) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-151"></a>
### External [151] On Path to Multimodal Generalist: General-Level and General-Bench (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** H. Fei, Y. Zhou, J. Li, X. Li, Q. Xu, B. Li, S. Wu, et al. On Path to Multimodal Generalist: General-Level and General-Bench, 2025. URL https://arxiv.org/abs/2505.04620.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2505.04620) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="demodiffusion-2025"></a>
### External [155] DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** S. Park, H. Bharadhwaj, and S. Tulsiani. DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy. arXiv preprint arXiv:2506.20668, 2025. URL https://arxiv.org/abs/2506.20668.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2506.20668) — transcribed from the external survey.

**Reading-note evidence:** [p. 17](https://arxiv.org/pdf/2609.36012v1#page=17).

- **Deployment context:** retargeted human motion used as an action proposal
- **Action mechanism:** a pretrained diffusion policy refines the retargeted motion proposal into the final robot motion
- **Deployment weights:** not detailed in the cited survey passage
- **Setting discussed:** hybrid of geometric correspondence and learned action generation
- **Survey evidence:** The survey contrasts DemoDiffusion’s learned refinement with IMOP’s direct transfer of a demonstrated end-effector pose.
- **Why read it:** Shows that using geometric correspondence does not make reference tracking the primary control interface.
- **Adaptation target:** motion transfer through a learned action prior
- **Evidence description:** method comparison in survey
- **Interpretation limit:** Retargeting quality and the learned diffusion prior both contribute to the final motion; the cited passage does not detail the physical evaluation protocol.

<a id="ref-168"></a>
### External [168] Hrt1: One-shot human-to-robot trajectory transfer for mobile manipulation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** S. H. Allu, Jishnu Jaykumar P, N. Khargonkar, T. Summers, J. Yao, and Y. Xiang. Hrt1: One-shot human-to-robot trajectory transfer for mobile manipulation, 2025. URL https://arxiv.org/abs/2510.21026.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2510.21026) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-172"></a>
### External [172] FUNCTO: Function-Centric One-Shot Imitation Learning for Tool Manipulation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** C. Tang, A. Xiao, Y. Deng, T. Hu, W. Dong, H. Zhang, D. Hsu, and H. Zhang. FUNCTO: Function-Centric One-Shot Imitation Learning for Tool Manipulation, 2025. URL https://arxiv.org/abs/2502.11744.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2502.11744) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-174"></a>
### External [174] GIFT: Geometry-Induced Functional Transfer for Category-level Object Manipulation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** C. de Farias, L. Figueredo, R. Laha, M. Adjigble, B. Tamadazte, R. Stolkin, S. Haddadin, and N. Marturi. GIFT: Geometry-Induced Functional Transfer for Category-level Object Manipulation, 2025. URL https://arxiv.org/abs/2503.15371.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2503.15371) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-177"></a>
### External [177] Annotation-Free One-Shot Imitation Learning for Multi-Step Manipulation Tasks (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** V. Wichitwechkarn, E. Williams, C. Fox, and R. Choudhary. Annotation-Free One-Shot Imitation Learning for Multi-Step Manipulation Tasks, 2025. URL https://arxiv.org/abs/2509.24972.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2509.24972) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-180"></a>
### External [180] A Comprehensive Survey on World Models for Embodied AI (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** X. Li, X. He, L. Zhang, M. Wu, X. Li, and Y. Liu. A Comprehensive Survey on World Models for Embodied AI. arXiv preprint arXiv:2510.16732, 2025. URL https://arxiv.org/abs/2510.16732.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2510.16732) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-190"></a>
### External [190] Point Policy: Unifying Observations and Actions with Key Points for Robot Manipulation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** S. Haldar and L. Pinto. Point Policy: Unifying Observations and Actions with Key Points for Robot Manipulation, 2025. URL https://arxiv.org/abs/2502.20391.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2502.20391) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-191"></a>
### External [191] Elastic Motion Policy: An Adaptive Dynamical System for Robust and Efficient One-Shot Imitation Learning (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** T. Li, S. Sun, S. S. Aditya, and N. Figueroa. Elastic Motion Policy: An Adaptive Dynamical System for Robust and Efficient One-Shot Imitation Learning, 2025. URL https://arxiv.org/abs/2503.08029.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2503.08029) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-193"></a>
### External [193] Spatialvla: Exploring spatial representations for visual-language-action model (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** D. Qu, H. Song, Q. Chen, Y. Yao, X. Ye, Y. Ding, Z. Wang, J. Gu, B. Zhao, D. Wang, and X. Li. Spatialvla: Exploring spatial representations for visual-language-action model. In Robotics: Science and Systems, 2025. URL https://arxiv.org/abs/2501.15830.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2501.15830) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-201"></a>
### External [201] Robust Instant Policy: Leveraging Student’s t-Regression Model for Robust In-context Imitation Learning of Robot Manipulation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** H. Oh, A. M. Salcedo-Vázquez, I. G. Ramirez-Alpizar, and Y. Domae. Robust Instant Policy: Leveraging Student’s t-Regression Model for Robust In-context Imitation Learning of Robot Manipulation. In IEEE/RSJ International Conference on Intelligent Robots and Systems, pages 7973–7980, 2025. doi: 10.1109/IROS60139.2025.11247005. URL https://arxiv.org/abs/2506.15157.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2506.15157) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-235"></a>
### External [235] Learning Long-Context Diffusion Policies via Past-Token Prediction (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** M. Torne, A. Tang, Y. Liu, and C. Finn. Learning Long-Context Diffusion Policies via Past-Token Prediction. arXiv preprint arXiv:2505.09561, 2025. URL https://arxiv.org/abs/2505.09561.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2505.09561) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-241"></a>
### External [241] RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dataset for Generalizable Embodied Intelligence (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** C. Hou, K. Wu, J. Liu, Z. Che, D. Wu, F. Liao, G. Li, J. He, Q. Feng, Z. Jin, C. Gu, Z. Liu, N. Han, X. Mi, Y. Lv, Y. Fu, G. Dai, L. Gu, T. Li, Y. Zhang, Y. Zhang, X. Wang, S. Fan, M. Li, Z. Zhao, N. Liu, Z. Xu, P. Ren, J. Ji, H. Liu, K. Cheng, S. Zhang, and J. Tang. RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dataset for Generalizable Embodied Intelligence, 2025. URL https://arxiv.org/abs/2512.24653.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2512.24653) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-242"></a>
### External [242] RoboCOIN: An Open-Sourced Bimanual Robotic Data Collection for Integrated Manipulation (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87), [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** S. Wu, X. Liu, S. Xie, P. Wang, X. Li, B. Yang, Z. Li, K. Zhu, H. Wu, Y. Liu, Z. Long, R. Xu, Y. Wang, C. Liu, D. Wang, Z. Ni, X. Yang, Y. Liu, R. Feng, L. Zhang, D. Huang, C. Jin, A. Yin, X. Wang, Z. Sun, J. Zhao, M. Du, M. Cao, X. Chen, H. Cheng, X. Zhang, Y. Fu, N. Chen, C. Chi, S. Chen, H. Lyu, X. Hao, Y. Wang, B. Lei, D. Liu, X. Yang, Y. Jiao, T. Pan, Y. Zhang, S. Wang, Z. Zhang, X. Liu, J. Zhang, C. Meng, Z. Zhang, J. Gao, S. Wang, X. Leng, Z. Xie, Z. Zhou, P. Huang, W. Yang, Y. Guo, Y. Zhu, S. Zheng, H. Cheng, X. Ding, Y. Yue, H. Wang, C. Chen, J. Pang, Y. Qian, H. Geng, L. Gao, H. Li, B. Fang, G. Huang, Y. Yang, H. Dong, H. Wang, H. Zhao, Y. Mu, D. Hu, H. Zhao, T. Huang, S. Zhang, Y. Lin, Z. Wang, and G. Yao. RoboCOIN: An Open-Sourced Bimanual Robotic Data Collection for Integrated Manipulation, 2025. URL https://arxiv.org/abs/2511.17441.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2511.17441) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-254"></a>
### External [254] Self-Improving Embodied Foundation Models (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** S. K. S. Ghasemipour, A. Wahid, J. Tompson, P. Sanketi, and I. Mordatch. Self-Improving Embodied Foundation Models, 2025. URL https://arxiv.org/abs/2509.15155.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2509.15155) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-257"></a>
### External [257] You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** H. Zhou, R. Wang, Y. Tai, Y. Deng, G. Liu, and K. Jia. You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations. In Robotics: Science and Systems, 2025. URL https://www.roboticsproceedings.org/rss21/p149.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://www.roboticsproceedings.org/rss21/p149.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-259"></a>
### External [259] Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** S. Yang, W. Yu, J. Zeng, J. Lv, K. Ren, C. Lu, D. Lin, and J. Pang. Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation. In Robotics: Science and Systems, 2025. URL https://www.roboticsproceedings.org/rss21/p146.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://www.roboticsproceedings.org/rss21/p146.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-266"></a>
### External [266] Is Diversity All You Need for Scalable Robotic Manipulation? (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** M. Shi, L. Chen, J. Chen, Y. Lu, C. Liu, G. Ren, P. Luo, D. Huang, M. Yao, and H. Li. Is Diversity All You Need for Scalable Robotic Manipulation?, 2025. URL https://arxiv.org/abs/2507.06219v1.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2507.06219v1) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-273"></a>
### External [273] π∗ 0.6: a VLA That Learns From Experience (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** Physical Intelligence et al. π∗ 0.6: a VLA That Learns From Experience, 2025. URL https://arxiv.org/abs/2511.14759.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2511.14759) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-280"></a>
### External [280] Emergence of Human to Robot Transfer in Vision-Language-Action Models (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** S. Kareer, K. Pertsch, J. Darpinian, J. Hoffman, D. Xu, S. Levine, C. Finn, and S. Nair. Emergence of Human to Robot Transfer in Vision-Language-Action Models, 2025. URL https://arxiv.org/abs/2512.22414.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2512.22414) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-282"></a>
### External [282] Action Tokenizer Matters in In-Context Imitation Learning (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** A. D. Vuong, M. N. Vu, D. An, and I. Reid. Action Tokenizer Matters in In-Context Imitation Learning. In IEEE/RSJ International Conference on Intelligent Robots and Systems, pages 13490–13496, 2025. doi: 10.1109/IROS60139.2025.11246836. URL https://arxiv.org/abs/2503.01206.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2503.01206) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-293"></a>
### External [293] Enabling Long(er) Horizon Imitation for Manipulation Tasks by Modeling Subgoal Transitions (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** S. Jain, S. Sachdeva, and R. Paul. Enabling Long(er) Horizon Imitation for Manipulation Tasks by Modeling Subgoal Transitions. In Conference on Robot Learning, 2025. URL https://proceedings.mlr.press/v305/jain25b.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://proceedings.mlr.press/v305/jain25b.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-305"></a>
### External [305] In-situ Value-aligned Human-Robot Interactions with Physical Constraints (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** H. Li, Z. Jiao, X. Liu, H. Liu, and Z. Zheng. In-situ Value-aligned Human-Robot Interactions with Physical Constraints. arXiv preprint arXiv:2508.07606, 2025. URL https://arxiv.org/abs/2508.07606.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2508.07606) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-310"></a>
### External [310] LIBERO-Plus: In-depth robustness analysis of vision-language-action models (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** S. Fei, S. Wang, J. Shi, Z. Dai, J. Cai, P. Qian, L. Ji, X. He, S. Zhang, Z. Fei, J. Fu, J. Gong, and X. Qiu. LIBERO-Plus: In-depth robustness analysis of vision-language-action models. arXiv preprint arXiv:2510.13626, 2025. URL https://arxiv.org/abs/2510.13626.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2510.13626) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-313"></a>
### External [313] Memory, Benchmark &amp; Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** E. Cherepanov, N. Kachaev, A. K. Kovalev, and A. I. Panov. Memory, Benchmark &amp; Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning. arXiv preprint arXiv:2502.10550, 2025. URL https://arxiv.org/abs/2502.10550.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2502.10550) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-315"></a>
### External [315] RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** J. Kwok, C. Agia, R. Sinha, M. Foutter, S. Li, I. Stoica, A. Mirhoseini, and M. Pavone. RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models, 2025. URL https://arxiv.org/abs/2506.17811.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2506.17811) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-327"></a>
### External [327] Self-Improving Loops for Visual Robotic Planning (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** C. Luo, Z. Zeng, M. Jia, Y. Du, and C. Sun. Self-Improving Loops for Visual Robotic Planning, 2025. URL https://arxiv.org/abs/2506.06658.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2506.06658) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-333"></a>
### External [333] Behavioral Exploration: Learning to Explore via In-Context Adaptation (2025)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** A. Wagenmaker, Z. Zhou, and S. Levine. Behavioral Exploration: Learning to Explore via In-Context Adaptation. arXiv preprint arXiv:2507.09041, 2025. URL https://arxiv.org/abs/2507.09041.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2507.09041) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-373"></a>
### External [373] Large VLM-based vision-language-action models for robotic manipulation: A survey (2025)

**Date basis:** Bibliography year. **Bibliography:** [p. 94](https://arxiv.org/pdf/2609.36012v1#page=94).

**Citation:** R. Shao, W. Li, L. Zhang, R. Zhang, Z. Liu, R. Chen, and L. Nie. Large VLM-based vision-language-action models for robotic manipulation: A survey, 2025. URL https://arxiv.org/abs/2508.13073.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2508.13073) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-35"></a>
### External [35] DITTO: Demonstration Imitation by Trajectory Transformation (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** N. Heppert, M. Argus, T. Welschehold, T. Brox, and A. Valada. DITTO: Demonstration Imitation by Trajectory Transformation. In IEEE/RSJ International Conference on Intelligent Robots and Systems, 2024. URL https://ditto.cs.uni-freiburg.de/.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://ditto.cs.uni-freiburg.de/) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-50"></a>
### External [50] Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** G. Tziafas and H. Kasaei. Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models, 2024. URL https://arxiv.org/abs/2406.18746.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2406.18746) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-58"></a>
### External [58] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** A. Khazatsky, K. Pertsch, S. Nair, A. Balakrishna, S. Dasari, S. Karamcheti, et al. DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset. arXiv preprint arXiv:2403.12945, 2024. URL https://arxiv.org/abs/2403.12945.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2403.12945) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-62"></a>
### External [62] Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** C. Chi, Z. Xu, C. Pan, E. Cousineau, B. Burchfiel, S. Feng, et al. Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots. arXiv preprint arXiv:2402.10329, 2024. URL https://arxiv.org/abs/2402.10329.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2402.10329) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-64"></a>
### External [64] HOT3D: Hand and Object Tracking in 3D from Egocentric Multi-View Videos (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** P. Banerjee, S. Shkodrani, P. Moulon, S. Hampali, S. Han, F. Zhang, L. Zhang, J. Fountain, E. Miller, S. Basol, R. Newcombe, R. Wang, J. J. Engel, and T. Hodan. HOT3D: Hand and Object Tracking in 3D from Egocentric Multi-View Videos, 2024. URL https://arxiv.org/abs/2411.19167.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2411.19167) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-75"></a>
### External [75] RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** S. Nasiriany, A. Maddukuri, L. Zhang, A. Parikh, A. Lo, A. Joshi, A. Mandlekar, and Y. Zhu. RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots, 2024. URL https://arxiv.org/abs/2406.02523.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2406.02523) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-76"></a>
### External [76] AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** M. Ahn, D. Dwibedi, C. Finn, M. G. Arenas, K. Gopalakrishnan, K. Hausman, B. Ichter, A. Irpan, N. Joshi, R. Julian, S. Kirmani, I. Leal, E. Lee, S. Levine, Y. Lu, I. Leal, S. Maddineni, K. Rao, D. Sadigh, P. Sanketi, P. Sermanet, Q. Vuong, S. Welker, F. Xia, T. Xiao, P. Xu, S. Xu, and Z. Xu. AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents, 2024. URL https://arxiv.org/abs/2401.12963.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2401.12963) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-80"></a>
### External [80] One-Shot Imitation under Mismatched Execution (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** K. Kedia, P. Dan, A. Chao, M. A. Pace, and S. Choudhury. One-Shot Imitation under Mismatched Execution. arXiv preprint arXiv:2409.06615, 2024. URL https://arxiv.org/abs/2409.06615.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2409.06615) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-81"></a>
### External [81] Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** C. Agia, R. Sinha, J. Yang, Z.-a. Cao, R. Antonova, M. Pavone, and J. Bohg. Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress. arXiv preprint arXiv:2410.04640, 2024. URL https://arxiv.org/abs/2410.04640.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2410.04640) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-85"></a>
### External [85] AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** J. Duan, W. Pumacay, N. Kumar, Y. R. Wang, S. Tian, W. Yuan, R. Krishna, D. Fox, A. Mandlekar, and Y. Guo. AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation, 2024. URL https://arxiv.org/abs/2410.00371.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2410.00371) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-87"></a>
### External [87] RACER: Rich Language-Guided Failure Recovery Policies for Imitation Learning (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** Y. Dai, J. Lee, N. Fazeli, and J. Chai. RACER: Rich Language-Guided Failure Recovery Policies for Imitation Learning, 2024. URL https://arxiv.org/abs/2409.14674.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2409.14674) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-116"></a>
### External [116] DrEureka: Language Model Guided Sim-To-Real Transfer (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** Y. J. Ma, W. Liang, H.-J. Wang, S. Wang, Y. Zhu, L. Fan, O. Bastani, and D. Jayaraman. DrEureka: Language Model Guided Sim-To-Real Transfer, 2024. URL https://arxiv.org/abs/2406.01967.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2406.01967) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-117"></a>
### External [117] Learning to Learn Faster from Human Feedback with Language Model Predictive Control (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** J. Liang, F. Xia, W. Yu, A. Zeng, M. G. Arenas, M. Attarian, M. Bauza, M. Bennice, A. Bewley, A. Dostmohamed, C. K. Fu, N. Gileadi, M. Giustina, K. Gopalakrishnan, L. Hasenclever, J. Humplik, J. Hsu, N. Joshi, B. Jyenis, C. Kew, S. Kirmani, T.-W. E. Lee, K.-H. Lee, A. H. Michaely, J. Moore, K. Oslund, D. Rao, A. Ren, B. Tabanpour, Q. Vuong, A. Wahid, T. Xiao, Y. Xu, V. Zhuang, P. Xu, E. Frey, K. Caluwaerts, T. Zhang, B. Ichter, J. Tompson, L. Takayama, V. Vanhoucke, I. Shafran, M. Mataric, D. Sadigh, N. Heess, K. Rao, N. Stewart, J. Tan, and C. Parada. Learning to Learn Faster from Human Feedback with Language Model Predictive Control, 2024. URL https://arxiv.org/abs/2402.11450.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2402.11450) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-118"></a>
### External [118] OpenVLA: An Open-Source Vision-Language-Action Model (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** M. J. Kim, K. Pertsch, S. Karamcheti, T. Xiao, A. Balakrishna, S. Nair, R. Rafailov, E. Foster, G. Lam, P. Sanketi, Q. Vuong, T. Kollar, B. Burchfiel, R. Tedrake, D. Sadigh, S. Levine, P. Liang, and C. Finn. OpenVLA: An Open-Source Vision-Language-Action Model. arXiv preprint arXiv:2406.09246, 2024. URL https://arxiv.org/abs/2406.09246.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2406.09246) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-119"></a>
### External [119] π0: A Vision-Language-Action Flow Model for General Robot Control (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, S. Jakubczak, T. Jones, L. Ke, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, K. Pertsch, L. X. Shi, J. Tanner, Q. Vuong, A. Walling, H. Wang, and U. Zhilinsky. π0: A Vision-Language-Action Flow Model for General Robot Control. arXiv preprint arXiv:2410.24164, 2024. URL https://arxiv.org/abs/2410.24164.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2410.24164) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-124"></a>
### External [124] A Survey on In-context Learning (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** Q. Dong, L. Li, D. Dai, C. Zheng, J. Ma, R. Li, H. Xia, J. Xu, Z. Wu, B. Chang, X. Sun, L. Li, and Z. Sui. A Survey on In-context Learning. In Conference on Empirical Methods in Natural Language Processing, pages 1107–1128, 2024. doi: 10.18653/v1/2024.emnlp-main.64. URL https://aclanthology.org/2024.emnlp-main.64/.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://aclanthology.org/2024.emnlp-main.64/) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-132"></a>
### External [132] Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** R. Doshi, H. Walke, O. Mees, S. Dasari, and S. Levine. Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation. arXiv preprint arXiv:2408.11812, 2024. URL https://arxiv.org/abs/2408.11812.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2408.11812) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="imop-2024"></a>
### External [156] One-Shot Imitation Learning with Invariance Matching for Robotic Manipulation (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** X. Zhang and A. Boularias. One-Shot Imitation Learning with Invariance Matching for Robotic Manipulation. In Robotics: Science and Systems, 2024. URL https://www.roboticsproceedings.org/rss20/p134.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://www.roboticsproceedings.org/rss20/p134.html) — transcribed from the external survey.

**Reading-note evidence:** [p. 17](https://arxiv.org/pdf/2609.36012v1#page=17), [p. 20](https://arxiv.org/pdf/2609.36012v1#page=20).

- **Deployment context:** a demonstration supplying the next end-effector pose
- **Action mechanism:** registration aligns the relevant demonstration transition and transfers an explicit target pose for execution
- **Deployment weights:** not detailed in the cited survey passage
- **Setting discussed:** geometric transfer of a demonstrated manipulation transition
- **Survey evidence:** The survey identifies the target pose as an executable reference and assigns more of the transfer burden to geometric applicability.
- **Why read it:** Contrasts direct reference transfer with learned refinement of a motion proposal.
- **Adaptation target:** geometric applicability of the demonstrated motion
- **Evidence description:** method comparison in survey
- **Interpretation limit:** The geometric match must remain applicable to the current scene; benchmark details and physical transfer results require the primary paper.

<a id="ref-165"></a>
### External [165] Vision-based Manipulation from Single Human Video with Open-World Object Graphs (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** Y. Zhu, A. Lim, P. Stone, and Y. Zhu. Vision-based Manipulation from Single Human Video with Open-World Object Graphs. arXiv preprint arXiv:2405.20321, 2024. URL https://arxiv.org/abs/2405.20321.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2405.20321) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-173"></a>
### External [173] One-Shot Manipulation Strategy Learning by Making Contact Analogies (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** Y. Liu, J. Mao, J. Tenenbaum, T. Lozano-Pérez, and L. P. Kaelbling. One-Shot Manipulation Strategy Learning by Making Contact Analogies, 2024. URL https://arxiv.org/abs/2411.09627.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2411.09627) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-189"></a>
### External [189] Keypoint Abstraction using Large Models for Object-Relative Imitation Learning (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** X. Fang, B.-R. Huang, J. Mao, J. Shone, J. B. Tenenbaum, T. Lozano-Pérez, and L. P. Kaelbling. Keypoint Abstraction using Large Models for Object-Relative Imitation Learning, 2024. URL https://arxiv.org/abs/2410.23254.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2410.23254) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-192"></a>
### External [192] Robopoint: A vision-language model for spatial affordance prediction for robotics (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** W. Yuan, J. Duan, V. Blukis, W. Pumacay, R. Krishna, A. Murali, A. Mousavian, and D. Fox. Robopoint: A vision-language model for spatial affordance prediction for robotics, 2024. URL https://arxiv.org/abs/2406.10721.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2406.10721) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-213"></a>
### External [213] MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** H. Singh, R. J. Das, M. Han, P. Nakov, and I. Laptev. MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation, 2024. URL https://arxiv.org/abs/2411.17636.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2411.17636) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-214"></a>
### External [214] Trust the PRoC3S: Solving Long-Horizon Robotics Problems with LLMs and Constraint Satisfaction (2024)

**Date basis:** Appendix A first public year; bibliography publication: 2025. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** A. Curtis, N. Kumar, J. Cao, T. Lozano-Pérez, and L. P. Kaelbling. Trust the PRoC3S: Solving Long-Horizon Robotics Problems with LLMs and Constraint Satisfaction. In Proceedings of The 8th Conference on Robot Learning, volume 270 of Proceedings of Machine Learning Research, pages 1362–1383, 2025. URL https://proceedings.mlr.press/v270/curtis25a.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://proceedings.mlr.press/v270/curtis25a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-215"></a>
### External [215] VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 86](https://arxiv.org/pdf/2609.36012v1#page=86).

**Citation:** G. Sarch, L. Jang, M. J. Tarr, W. W. Cohen, K. Marino, and K. Fragkiadaki. VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought. In Advances in Neural Information Processing Systems, volume 37, 2024. URL https://papers.nips.cc/paper\_files/paper/2024/hash/ 8ac50fd0a4eeeb1f077b17bb7c5353c3-Abstract-Conference.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://papers.nips.cc/paper_files/paper/2024/hash/8ac50fd0a4eeeb1f077b17bb7c5353c3-Abstract-Conference.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-224"></a>
### External [224] Fastumi: A scalable and hardware-independent universal manipulation interface with dataset (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** Zhaxizhuoma, K. Liu, C. Guan, Z. Jia, Z. Wu, X. Liu, T. Wang, S. Liang, P. Chen, P. Zhang, H. Song, D. Qu, D. Wang, Z. Wang, N. Cao, Y. Ding, B. Zhao, and X. Li. Fastumi: A scalable and hardware-independent universal manipulation interface with dataset, 2024. URL https://arxiv.org/abs/2409.19499.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2409.19499) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-225"></a>
### External [225] Umi on legs: Making manipulation policies mobile with manipulation-centric whole-body controllers (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** H. Ha, Y. Gao, Z. Fu, J. Tan, and S. Song. Umi on legs: Making manipulation policies mobile with manipulation-centric whole-body controllers. In Conference on Robot Learning, 2024. URL https://arxiv.org/abs/2407.10353.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2407.10353) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-240"></a>
### External [240] RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** K. Wu, C. Hou, J. Liu, Z. Che, X. Ju, Z. Yang, M. Li, Y. Zhao, Z. Xu, G. Yang, S. Fan, X. Wang, F. Liao, Z. Zhao, G. Li, Z. Jin, L. Wang, J. Mao, N. Liu, P. Ren, Q. Zhang, Y. Lyu, M. Liu, J. He, Y. Luo, Z. Gao, C. Li, C. Gu, Y. Fu, D. Wu, X. Wang, S. Chen, Z. Wang, P. An, S. Qian, S. Zhang, and J. Tang. RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation, 2024. URL https://arxiv.org/abs/2412.13877.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2412.13877) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-275"></a>
### External [275] Octo: An Open-Source Generalist Robot Policy (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** Octo Model Team, D. Ghosh, H. Walke, K. Pertsch, K. Black, O. Mees, S. Dasari, J. Hejna, T. Kreiman, C. Xu, J. Luo, Y. L. Tan, L. Y. Chen, P. Sanketi, Q. Vuong, T. Xiao, D. Sadigh, C. Finn, and S. Levine. Octo: An Open-Source Generalist Robot Policy. arXiv preprint arXiv:2405.12213, 2024. URL https://arxiv.org/abs/2405.12213.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2405.12213) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-278"></a>
### External [278] Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** L. Wang, X. Chen, J. Zhao, and K. He. Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers, 2024. URL https://arxiv.org/abs/2409.20537.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2409.20537) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-279"></a>
### External [279] RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** S. Liu, L. Wu, B. Li, H. Tan, H. Chen, Z. Wang, K. Xu, H. Su, and J. Zhu. RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation. arXiv preprint arXiv:2410.07864, 2024. URL https://arxiv.org/abs/2410.07864.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2410.07864) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-295"></a>
### External [295] ScrewMimic: Bimanual Imitation from Human Videos with Screw Space Projection (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** A. Bahety, P. Mandikal, B. Abbatematteo, and R. Martín-Martín. ScrewMimic: Bimanual Imitation from Human Videos with Screw Space Projection. In Robotics: Science and Systems, 2024. URL https://www.roboticsproceedings.org/rss20/p078.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://www.roboticsproceedings.org/rss20/p078.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-298"></a>
### External [298] Introspective Planning: Aligning Robots’ Uncertainty with Inherent Task Ambiguity (2024)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** K. Liang, Z. Zhang, and J. F. Fisac. Introspective Planning: Aligning Robots’ Uncertainty with Inherent Task Ambiguity. arXiv preprint arXiv:2402.06529, 2024. URL https://arxiv.org/abs/2402.06529.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2402.06529) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-319"></a>
### External [319] Parallel Structures in Pre-training Data Yield In-Context Learning (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** Y. Chen, C. Zhao, Z. Yu, K. McKeown, and H. He. Parallel Structures in Pre-training Data Yield In-Context Learning. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 8582–8592, 2024. doi: 10.18653/v1/2024.acl-long.465. URL https://aclanthology.org/2024.acl-long.465/.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://aclanthology.org/2024.acl-long.465/) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-322"></a>
### External [322] Position: Do Pretrained Transformers Learn In-Context by Gradient Descent? (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** L. Shen, A. Mishra, and D. Khashabi. Position: Do Pretrained Transformers Learn In-Context by Gradient Descent? In International Conference on Machine Learning, volume 235 of Proceedings of Machine Learning Research, pages 44712–44740, 2024. URL https://proceedings.mlr.press/v235/shen24d.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://proceedings.mlr.press/v235/shen24d.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-331"></a>
### External [331] EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** A. Zala, J. Cho, H. Lin, J. Yoon, and M. Bansal. EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents, 2024. URL https://arxiv.org/abs/2403.12014.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2403.12014) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-332"></a>
### External [332] OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code (2024)

**Date basis:** Bibliography year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** M. Faldor, J. Zhang, A. Cully, and J. Clune. OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code, 2024. URL https://arxiv.org/abs/2405.15568.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2405.15568) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-351"></a>
### External [351] NOLO: Navigate Only Look Once (2024)

**Date basis:** Appendix A first public year; bibliography publication: 2025. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** B. Zhou, Z. Zhang, J. Wang, and Z. Lu. NOLO: Navigate Only Look Once. In 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 17162–17169. IEEE, October 2025. doi: 10.1109/iros60139.2025.11246428. URL http://dx.doi.org/10.1109/IROS60139.2025.11246428.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](http://dx.doi.org/10.1109/IROS60139.2025.11246428) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-352"></a>
### External [352] Select2Plan: Training-Free ICL-Based Planning Through VQA and Memory Retrieval (2024)

**Date basis:** Appendix A first public year; bibliography publication: 2025. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** D. Buoso, L. Robinson, G. Averta, P. Torr, T. Franzmeyer, and D. De Martini. Select2Plan: Training-Free ICL-Based Planning Through VQA and Memory Retrieval. IEEE Robotics and Automation Letters, 10(11): 11267–11274, November 2025. ISSN 2377-3774. doi: 10.1109/lra.2025.3606790. URL http://dx.doi.org/10.1109/LRA.2025.3606790.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](http://dx.doi.org/10.1109/LRA.2025.3606790) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-353"></a>
### External [353] VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments (2024)

**Date basis:** Appendix A first public year; bibliography publication: 2025. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** M. Elnoor, K. Weerakoon, G. Seneviratne, R. Xian, T. Guan, M. K. M Jaffar, V. Rajagopal, and D. Manocha. VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments. In 2025 IEEE International Conference on Robotics and Automation (ICRA), pages 2391–2398. IEEE, May 2025. doi: 10.1109/icra55743.2025.11128264. URL http://dx.doi.org/10.1109/ICRA55743.2025.11128264.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](http://dx.doi.org/10.1109/ICRA55743.2025.11128264) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-20"></a>
### External [20] Metadiffuser: Diffusion model as conditional planner for offline meta-rl (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** F. Ni, J. Hao, Y. Mu, Y. Yuan, Y. Zheng, B. Wang, and Z. Liang. Metadiffuser: Diffusion model as conditional planner for offline meta-rl. In International Conference on Machine Learning, 2023. URL https://proceedings.mlr.press/v202/ni23a.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://proceedings.mlr.press/v202/ni23a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-46"></a>
### External [46] Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** L. Zha, Y. Cui, L.-H. Lin, M. Kwon, M. G. Arenas, A. Zeng, F. Xia, and D. Sadigh. Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections. arXiv preprint arXiv:2311.10678, 2023. URL https://arxiv.org/abs/2311.10678.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2311.10678) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-56"></a>
### External [56] BridgeData V2: A Dataset for Robot Learning at Scale (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78), [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** H. Walke, K. Black, A. Lee, M. J. Kim, M. Du, C. Zheng, T. Zhao, P. Hansen-Estruch, Q. Vuong, A. He, V. Myers, K. Fang, C. Finn, and S. Levine. BridgeData V2: A Dataset for Robot Learning at Scale. arXiv preprint arXiv:2308.12952, 2023. URL https://arxiv.org/abs/2308.12952.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2308.12952) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-57"></a>
### External [57] Open X-Embodiment: Robotic Learning Datasets and RT-X Models (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** Open X-Embodiment Collaboration. Open X-Embodiment: Robotic Learning Datasets and RT-X Models. arXiv preprint arXiv:2310.08864, 2023. URL https://arxiv.org/abs/2310.08864.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2310.08864) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-59"></a>
### External [59] RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** H.-S. Fang, H. Fang, Z. Tang, J. Liu, C. Wang, J. Wang, et al. RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot. arXiv preprint arXiv:2307.00595, 2023. URL https://arxiv.org/abs/2307.00595.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2307.00595) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-70"></a>
### External [70] Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** K. Grauman, A. Westbury, L. Torresani, K. Kitani, J. Malik, T. Afouras, K. Ashutosh, V. Baiyya, S. Bansal, B. Boote, E. Byrne, Z. Chavis, J. Chen, F. Cheng, F.-J. Chu, S. Crane, A. Dasgupta, J. Dong, M. Escobar, C. Forigua, A. Gebreselasie, S. Haresh, J. Huang, M. M. Islam, S. Jain, R. Khirodkar, D. Kukreja, K. J. Liang, J.-W. Liu, S. Majumder, Y. Mao, M. Martin, E. Mavroudi, T. Nagarajan, F. Ragusa, S. K. Ramakrishnan, L. Seminara, A. Somayazulu, Y. Song, S. Su, Z. Xue, E. Zhang, J. Zhang, A. Castillo, C. Chen, X. Fu, R. Furuta, C. Gonzalez, P. Gupta, J. Hu, Y. Huang, Y. Huang, W. Khoo, A. Kumar, R. Kuo, S. Lakhavani, M. Liu, M. Luo, Z. Luo, B. Meredith, A. Miller, O. Oguntola, X. Pan, P. Peng, S. Pramanick, M. Ramazanova, F. Ryan, W. Shan, K. Somasundaram, C. Song, A. Southerland, M. Tateno, H. Wang, Y. Wang, T. Yagi, M. Yan, X. Yang, Z. Yu, S. C. Zha, C. Zhao, Z. Zhao, Z. Zhu, J. Zhuo, P. Arbelaez, G. Bertasius, D. Crandall, D. Damen, J. Engel, G. M. Farinella, A. Furnari, B. Ghanem, J. Hoffman, C. V. Jawahar, R. Newcombe, H. S. Park, J. M. Rehg, Y. Sato, M. Savva, J. Shi, M. Z. Shou, and M. Wray. Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives. arXiv preprint arXiv:2311.18259, 2023. URL https://arxiv.org/abs/2311.18259.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2311.18259) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-73"></a>
### External [73] HoloAssist: an Egocentric Human Interaction Dataset for Interactive AI Assistants in the Real World (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** X. Wang, T. Kwon, M. Rad, B. Pan, I. Chakraborty, S. Andrist, D. Bohus, A. Feniello, B. Tekin, F. V. Frujeri, N. Joshi, and M. Pollefeys. HoloAssist: an Egocentric Human Interaction Dataset for Interactive AI Assistants in the Real World, 2023. URL https://arxiv.org/abs/2309.17024.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2309.17024) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-74"></a>
### External [74] MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** A. Mandlekar, S. Nasiriany, B. Wen, I. Akinola, Y. Narang, L. Fan, Y. Zhu, and D. Fox. MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations. arXiv preprint arXiv:2310.17596, 2023. URL https://arxiv.org/abs/2310.17596.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2310.17596) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-84"></a>
### External [84] REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** Z. Liu, A. Bahety, and S. Song. REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction, 2023. URL https://arxiv.org/abs/2306.15724.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2306.15724) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-86"></a>
### External [86] Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** A. Z. Ren, A. Dixit, A. Bodrova, S. Singh, S. Tu, N. Brown, P. Xu, L. Takayama, F. Xia, J. Varley, Z. Xu, D. Sadigh, A. Zeng, and A. Majumdar. Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners. arXiv preprint arXiv:2307.01928, 2023. URL https://arxiv.org/abs/2307.01928.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2307.01928) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-96"></a>
### External [96] SayTap: Language to Quadrupedal Locomotion (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** Y. Tang, W. Yu, J. Tan, H. Zen, A. Faust, and T. Harada. SayTap: Language to Quadrupedal Locomotion. arXiv preprint arXiv:2306.07580, 2023. URL https://arxiv.org/abs/2306.07580.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2306.07580) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-112"></a>
### External [112] Transformers Learn In-Context by Gradient Descent (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** J. Von Oswald, E. Niklasson, E. Randazzo, J. Sacramento, A. Mordvintsev, A. Zhmoginov, and M. Vladymyrov. Transformers Learn In-Context by Gradient Descent. In International Conference on Machine Learning, volume 202 of Proceedings of Machine Learning Research, pages 35151–35174, 2023. URL https://proceedings.mlr.press/v202/von-oswald23a.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://proceedings.mlr.press/v202/von-oswald23a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-114"></a>
### External [114] RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** K. Bousmalis, G. Vezzani, D. Rao, C. Devin, A. X. Lee, M. Bauza, T. Davchev, Y. Zhou, A. Gupta, A. Raju, A. Laurens, C. Fantacci, V. Dalibard, M. Zambelli, M. Martins, R. Pevceviciute, M. Blokzijl, M. Denil, N. Batchelor, T. Lampe, E. Parisotto, K. Żołna, S. Reed, S. G. Colmenarejo, J. Scholz, A. Abdolmaleki, O. Groth, J.-B. Regli, O. Sushkov, T. Rothörl, J. E. Chen, Y. Aytar, D. Barker, J. Ortiz, M. Riedmiller, J. T. Springenberg, R. Hadsell, F. Nori, and N. Heess. RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation, 2023. URL https://arxiv.org/abs/2306.11706.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2306.11706) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-115"></a>
### External [115] Eureka: Human-Level Reward Design via Coding Large Language Models (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** Y. J. Ma, W. Liang, G. Wang, D.-A. Huang, O. Bastani, D. Jayaraman, Y. Zhu, L. Fan, and A. Anandkumar. Eureka: Human-Level Reward Design via Coding Large Language Models, 2023. URL https://arxiv.org/abs/2310.12931.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2310.12931) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-141"></a>
### External [141] Self-Improving Robots: End-to-End Autonomous Visuomotor Reinforcement Learning (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** A. Sharma, A. M. Ahmed, R. Ahmad, and C. Finn. Self-Improving Robots: End-to-End Autonomous Visuomotor Reinforcement Learning, 2023. URL https://arxiv.org/abs/2303.01488.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2303.01488) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-164"></a>
### External [164] One-shot Visual Imitation via Attributed Waypoints and Demonstration Augmentation (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** M. Chang and S. Gupta. One-shot Visual Imitation via Attributed Waypoints and Demonstration Augmentation. arXiv preprint arXiv:2302.04856, 2023. URL https://arxiv.org/abs/2302.04856.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2302.04856) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-169"></a>
### External [169] RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** M. Vecerik, C. Doersch, Y. Yang, T. Davchev, Y. Aytar, G. Zhou, R. Hadsell, L. Agapito, and J. Scholz. RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation, 2023. URL https://arxiv.org/abs/2308.15975.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2308.15975) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-170"></a>
### External [170] One-Shot Imitation Learning: A Pose Estimation Perspective (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** P. Vitiello, K. Dreczkowski, and E. Johns. One-Shot Imitation Learning: A Pose Estimation Perspective. In Conference on Robot Learning, 2023. URL https://proceedings.mlr.press/v229/vitiello23a.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://proceedings.mlr.press/v229/vitiello23a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-171"></a>
### External [171] One-shot Imitation Learning via Interaction Warping (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** O. Biza, S. Thompson, K. R. Pagidi, A. Kumar, E. van der Pol, R. Walters, T. Kipf, J.-W. van de Meent, L. L. S. Wong, and R. Platt. One-shot Imitation Learning via Interaction Warping. In Conference on Robot Learning, 2023. URL https://proceedings.mlr.press/v229/biza23a.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://proceedings.mlr.press/v229/biza23a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-184"></a>
### External [184] VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** W. Huang, C. Wang, R. Zhang, Y. Li, J. Wu, and L. Fei-Fei. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models. arXiv preprint arXiv:2307.05973, 2023. URL https://arxiv.org/abs/2307.05973.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2307.05973) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-228"></a>
### External [228] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** B. Liu, Y. Zhu, C. Gao, Y. Feng, Q. Liu, Y. Zhu, and P. Stone. LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning. arXiv preprint arXiv:2306.03310, 2023. URL https://arxiv.org/abs/2306.03310.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2306.03310) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-229"></a>
### External [229] Maniskill2: A unified benchmark for generalizable manipulation skills (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** J. Gu, F. Xiang, X. Li, Z. Ling, X. Liu, T. Mu, Y. Tang, S. Tao, X. Wei, Y. Yao, X. Yuan, P. Xie, Z. Huang, R. Chen, and H. Su. Maniskill2: A unified benchmark for generalizable manipulation skills. In International Conference on Learning Representations, 2023. URL https://arxiv.org/abs/2302.04659.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/2302.04659) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-232"></a>
### External [232] The mechanistic basis of data dependence and abrupt learning in an in-context classification task (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** G. Reddy. The mechanistic basis of data dependence and abrupt learning in an in-context classification task. arXiv preprint arXiv:2312.03002, 2023. URL https://arxiv.org/abs/2312.03002.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2312.03002) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-243"></a>
### External [243] RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** H. Bharadhwaj, J. Vakil, M. Sharma, A. Gupta, S. Tulsiani, and V. Kumar. RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking. arXiv preprint arXiv:2309.01918, 2023. URL https://arxiv.org/abs/2309.01918.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2309.01918) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-251"></a>
### External [251] MimicPlay: Long-Horizon Imitation Learning by Watching Human Play (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** C. Wang, L. Fan, J. Sun, R. Zhang, L. Fei-Fei, D. Xu, Y. Zhu, and A. Anandkumar. MimicPlay: Long-Horizon Imitation Learning by Watching Human Play. arXiv preprint arXiv:2302.12422, 2023. URL https://arxiv.org/abs/2302.12422.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2302.12422) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-253"></a>
### External [253] Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 88](https://arxiv.org/pdf/2609.36012v1#page=88).

**Citation:** A. Raventós, M. Paul, F. Chen, and S. Ganguli. Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression. arXiv preprint arXiv:2306.15063, 2023. URL https://arxiv.org/abs/2306.15063.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2306.15063) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-274"></a>
### External [274] Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** T. Z. Zhao, V. Kumar, S. Levine, and C. Finn. Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware. arXiv preprint arXiv:2304.13705, 2023. URL https://arxiv.org/abs/2304.13705.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2304.13705) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-277"></a>
### External [277] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choromanski, T. Ding, D. Driess, A. Dubey, C. Finn, P. Florence, C. Fu, M. G. Arenas, K. Gopalakrishnan, K. Han, K. Hausman, A. Herzog, J. Hsu, B. Ichter, A. Irpan, N. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, I. Leal, L. Lee, T.-W. E. Lee, S. Levine, Y. Lu, H. Michalewski, I. Mordatch, K. Pertsch, K. Rao, K. Reymann, M. Ryoo, G. Salazar, P. Sanketi, P. Sermanet, J. Singh, A. Singh, R. Soricut, H. Tran, V. Vanhoucke, Q. Vuong, A. Wahid, S. Welker, P. Wohlhart, J. Wu, F. Xia, T. Xiao, P. Xu, S. Xu, T. Yu, and B. Zitkovich. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. arXiv preprint arXiv:2307.15818, 2023. URL https://arxiv.org/abs/2307.15818.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2307.15818) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-323"></a>
### External [323] Are emergent abilities of large language models a mirage? (2023)

**Date basis:** Bibliography year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** R. Schaeffer, B. Miranda, and S. Koyejo. Are emergent abilities of large language models a mirage? arXiv preprint arXiv:2304.15004, 2023. URL https://arxiv.org/abs/2304.15004.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2304.15004) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-360"></a>
### External [360] A2Nav: Action-Aware Zero-Shot Robot Navigation by Exploiting Vision-and-Language Ability of Foundation Models (2023)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** P. Chen, X. Sun, H. Zhi, R. Zeng, T. H. Li, G. Liu, M. Tan, and C. Gan. A2Nav: Action-Aware Zero-Shot Robot Navigation by Exploiting Vision-and-Language Ability of Foundation Models, 2023. URL https://arxiv.org/abs/2308.07997.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2308.07997) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="prompt-dt-2022"></a>
### External [5] Prompting Decision Transformer for Few-Shot Policy Generalization (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 76](https://arxiv.org/pdf/2609.36012v1#page=76).

**Citation:** M. Xu, Y. Shen, S. Zhang, Y. Lu, D. Zhao, J. B. Tenenbaum, et al. Prompting Decision Transformer for Few-Shot Policy Generalization. arXiv preprint arXiv:2206.13499, 2022. URL https://arxiv.org/abs/2206.13499.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2206.13499) — transcribed from the external survey.

**Reading-note evidence:** [p. 4](https://arxiv.org/pdf/2609.36012v1#page=4), [p. 13](https://arxiv.org/pdf/2609.36012v1#page=13).

- **Deployment context:** trajectory prompts containing earlier observations and actions
- **Action mechanism:** a sequence policy uses trajectory evidence to condition later decisions
- **Deployment weights:** not detailed in the cited survey passages
- **Setting discussed:** historical trajectory-model route to few-shot policy generalization
- **Survey evidence:** The survey places Prompt-DT among sequence interfaces that retain observations and actions as evidence for later decisions.
- **Why read it:** Provides an early trajectory-prompting reference in the development of contextual policies.
- **Adaptation target:** policy generalization through trajectory prompts
- **Evidence description:** historical discussion in survey
- **Interpretation limit:** The survey discusses trajectory prompting; it does not provide a complete benchmark protocol or an exact prompt budget.

<a id="ref-19"></a>
### External [19] Decomposed mutual information optimization for generalized context in meta-reinforcement learning (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** Y. Mu, Y. Zhuang, F. Ni, B. Wang, J. Chen, J. Hao, and P. Luo. Decomposed mutual information optimization for generalized context in meta-reinforcement learning. In Advances in Neural Information Processing Systems, 2022. URL https://arxiv.org/abs/2210.04209.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/2210.04209) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-27"></a>
### External [27] Code as Policies: Language Model Programs for Embodied Control (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** J. Liang, W. Huang, F. Xia, P. Xu, K. Hausman, B. Ichter, et al. Code as Policies: Language Model Programs for Embodied Control. arXiv preprint arXiv:2209.07753, 2022. URL https://arxiv.org/abs/2209.07753.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2209.07753) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-28"></a>
### External [28] ProgPrompt: Generating Situated Robot Task Plans using Large Language Models (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** I. Singh, V. Blukis, A. Mousavian, A. Goyal, D. Xu, J. Tremblay, D. Fox, J. Thomason, and A. Garg. ProgPrompt: Generating Situated Robot Task Plans using Large Language Models. arXiv preprint arXiv:2209.11302, 2022. URL https://arxiv.org/abs/2209.11302.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2209.11302) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-33"></a>
### External [33] Demonstrate Once, Imitate Immediately (DOME): Learning Visual Servoing for One-Shot Imitation Learning (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** E. Valassakis, G. Papagiannis, N. Di Palo, and E. Johns. Demonstrate Once, Imitate Immediately (DOME): Learning Visual Servoing for One-Shot Imitation Learning. In IEEE/RSJ International Conference on Intelligent Robots and Systems, 2022. URL https://arxiv.org/abs/2204.02863.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2204.02863) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-63"></a>
### External [63] HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** Y. Liu, Y. Liu, C. Jiang, K. Lyu, W. Wan, H. Shen, B. Liang, Z. Fu, H. Wang, and L. Yi. HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction, 2022. URL https://arxiv.org/abs/2203.01577.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2203.01577) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-72"></a>
### External [72] Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** F. Sener, D. Chatterjee, D. Shelepov, K. He, D. Singhania, R. Wang, and A. Yao. Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities, 2022. URL https://arxiv.org/abs/2203.14712.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2203.14712) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-111"></a>
### External [111] Data distributional properties drive emergent in-context learning in transformers (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** S. C. Y. Chan, A. Santoro, A. K. Lampinen, J. X. Wang, A. Singh, P. H. Richemond, J. McClelland, and F. Hill. Data distributional properties drive emergent in-context learning in transformers. arXiv preprint arXiv:2205.05055, 2022. URL https://arxiv.org/abs/2205.05055.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2205.05055) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-113"></a>
### External [113] MetaICL: Learning to Learn In Context (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 81](https://arxiv.org/pdf/2609.36012v1#page=81).

**Citation:** S. Min, M. Lewis, L. Zettlemoyer, and H. Hajishirzi. MetaICL: Learning to Learn In Context. In Proceedings of NAACL-HLT, 2022. URL https://arxiv.org/abs/2110.15943v2.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2110.15943v2) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-131"></a>
### External [131] REvolveR: Continuous Evolutionary Models for Robot-to-robot Policy Transfer (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** X. Liu, D. Pathak, and K. Kitani. REvolveR: Continuous Evolutionary Models for Robot-to-robot Policy Transfer. In Proceedings of the 39th International Conference on Machine Learning, volume 162 of Proceedings of Machine Learning Research, pages 13995–14007, 2022. URL https://proceedings.mlr.press/v162/liu22p.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://proceedings.mlr.press/v162/liu22p.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-144"></a>
### External [144] Meta-Learning in Neural Networks: A Survey (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** T. Hospedales, A. Antoniou, P. Micaelli, and A. Storkey. Meta-Learning in Neural Networks: A Survey. IEEE Transactions on Pattern Analysis and Machine Intelligence, 44(9):5149–5169, 2022. doi: 10.1109/TPAMI.2021.3079209. URL https://arxiv.org/abs/2004.05439.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2004.05439) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-150"></a>
### External [150] Human-to-Robot Imitation in the Wild (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** S. Bahl, A. Gupta, and D. Pathak. Human-to-Robot Imitation in the Wild. arXiv preprint arXiv:2207.09450, 2022. URL https://human2robot.github.io/resources/paper.pdf.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://human2robot.github.io/resources/paper.pdf) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-185"></a>
### External [185] Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** M. Ahn, A. Brohan, N. Brown, Y. Chebotar, O. Cortes, B. David, C. Finn, C. Fu, K. Gopalakrishnan, K. Hausman, A. Herzog, D. Ho, J. Hsu, J. Ibarz, B. Ichter, A. Irpan, E. Jang, R. J. Ruano, K. Jeffrey, S. Jesmonth, N. J. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, K.-H. Lee, S. Levine, Y. Lu, L. Luu, C. Parada, P. Pastor, J. Quiambao, K. Rao, J. Rettinghouse, D. Reyes, P. Sermanet, N. Sievers, C. Tan, A. Toshev, V. Vanhoucke, F. Xia, T. Xiao, P. Xu, S. Xu, M. Yan, and A. Zeng. Do As I Can, Not As I Say: Grounding Language in Robotic Affordances. arXiv preprint arXiv:2204.01691, 2022. URL https://arxiv.org/abs/2204.01691.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2204.01691) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-186"></a>
### External [186] Inner Monologue: Embodied Reasoning through Planning with Language Models (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** W. Huang, F. Xia, T. Xiao, H. Chan, J. Liang, P. Florence, A. Zeng, J. Tompson, I. Mordatch, Y. Chebotar, P. Sermanet, N. Brown, T. Jackson, L. Luu, S. Levine, K. Hausman, and B. Ichter. Inner Monologue: Embodied Reasoning through Planning with Language Models. arXiv preprint arXiv:2207.05608, 2022. URL https://arxiv.org/abs/2207.05608.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/2207.05608) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-197"></a>
### External [197] Robust Task Representations for Offline Meta-Reinforcement Learning via Contrastive Learning (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** H. Yuan and Z. Lu. Robust Task Representations for Offline Meta-Reinforcement Learning via Contrastive Learning. arXiv preprint arXiv:2206.10442, 2022. URL https://arxiv.org/abs/2206.10442.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2206.10442) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-276"></a>
### External [276] RT-1: Robotics Transformer for Real-World Control at Scale (2022)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, J. Hsu, J. Ibarz, B. Ichter, A. Irpan, T. Jackson, S. Jesmonth, N. J. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, I. Leal, K.-H. Lee, S. Levine, Y. Lu, U. Malla, D. Manjunath, I. Mordatch, O. Nachum, C. Parada, J. Peralta, E. Perez, K. Pertsch, J. Quiambao, K. Rao, M. Ryoo, G. Salazar, P. Sanketi, K. Sayed, J. Singh, S. Sontakke, A. Stone, C. Tan, H. Tran, V. Vanhoucke, S. Vega, Q. Vuong, F. Xia, T. Xiao, P. Xu, S. Xu, T. Yu, and B. Zitkovich. RT-1: Robotics Transformer for Real-World Control at Scale. arXiv preprint arXiv:2212.06817, 2022. URL https://arxiv.org/abs/2212.06817.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2212.06817) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-320"></a>
### External [320] Rethinking the role of demonstrations: What makes in-context learning work? (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91), [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** S. Min, X. Lyu, A. Holtzman, M. Artetxe, M. Lewis, H. Hajishirzi, and L. Zettlemoyer. Rethinking the role of demonstrations: What makes in-context learning work? In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 11048–11064, 2022. doi: 10.18653/v1/2022.emnlp-main.759. URL https://aclanthology.org/2022.emnlp-main.759/.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://aclanthology.org/2022.emnlp-main.759/) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-321"></a>
### External [321] What can transformers learn in-context? a case study of simple function classes (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** S. Garg, D. Tsipras, P. Liang, and G. Valiant. What can transformers learn in-context? a case study of simple function classes. arXiv preprint arXiv:2208.01066, 2022. URL https://arxiv.org/abs/2208.01066.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2208.01066) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-324"></a>
### External [324] Scaling Instruction-Finetuned Language Models (2022)

**Date basis:** Bibliography year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** H. W. Chung, L. Hou, S. Longpre, B. Zoph, Y. Tay, W. Fedus, et al. Scaling Instruction-Finetuned Language Models. arXiv preprint arXiv:2210.11416, 2022. URL https://arxiv.org/abs/2210.11416v5.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2210.11416v5) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-346"></a>
### External [346] SE(3)-Equivariant Relational Rearrangement with Neural Descriptor Fields (2022)

**Date basis:** Appendix A first public year; bibliography publication: 2023. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** A. Simeonov, Y. Du, Y.-C. Lin, A. Rodriguez Garcia, L. P. Kaelbling, T. Lozano-Perez, and P. Agrawal. SE(3)-Equivariant Relational Rearrangement with Neural Descriptor Fields. In Proceedings of The 6th Conference on Robot Learning, volume 205 of Proceedings of Machine Learning Research, pages 835–846, 2023. URL https://proceedings.mlr.press/v205/simeonov23a.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://proceedings.mlr.press/v205/simeonov23a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-359"></a>
### External [359] LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action (2022)

**Date basis:** Appendix A first public year; bibliography publication: 2023. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** D. Shah, B. Osiński, B. Ichter, and S. Levine. LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action. In K. Liu, D. Kulic, and J. Ichnowski, editors, Proceedings of The 6th Conference on Robot Learning, volume 205 of Proceedings of Machine Learning Research, pages 492–504. PMLR, 14–18 Dec 2023. URL https://proceedings.mlr.press/v205/shah23b.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://proceedings.mlr.press/v205/shah23b.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-12"></a>
### External [12] Towards More Generalizable One-shot Visual Imitation Learning (2021)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** Z. Mandi, F. Liu, K. Lee, and P. Abbeel. Towards More Generalizable One-shot Visual Imitation Learning. arXiv preprint arXiv:2110.13423, 2021. URL https://arxiv.org/abs/2110.13423.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2110.13423) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-68"></a>
### External [68] Ego4D: Around the World in 3,000 Hours of Egocentric Video (2021)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** K. Grauman, A. Westbury, E. Byrne, Z. Chavis, A. Furnari, R. Girdhar, J. Hamburger, H. Jiang, M. Liu, X. Liu, M. Martin, T. Nagarajan, I. Radosavovic, S. K. Ramakrishnan, F. Ryan, J. Sharma, M. Wray, M. Xu, E. Z. Xu, C. Zhao, S. Bansal, D. Batra, V. Cartillier, S. Crane, T. Do, M. Doulaty, A. Erapalli, C. Feichtenhofer, A. Fragomeni, Q. Fu, A. Gebreselasie, C. Gonzalez, J. Hillis, X. Huang, Y. Huang, W. Jia, W. Khoo, J. Kolar, S. Kottur, A. Kumar, F. Landini, C. Li, Y. Li, Z. Li, K. Mangalam, R. Modhugu, J. Munro, T. Murrell, T. Nishiyasu, W. Price, P. R. Puentes, M. Ramazanova, L. Sari, K. Somasundaram, A. Southerland, Y. Sugano, R. Tao, M. Vo, Y. Wang, X. Wu, T. Yagi, Z. Zhao, Y. Zhu, P. Arbelaez, D. Crandall, D. Damen, G. M. Farinella, C. Fuegen, B. Ghanem, V. K. Ithapu, C. V. Jawahar, H. Joo, K. Kitani, H. Li, R. Newcombe, A. Oliva, H. S. Park, J. M. Rehg, Y. Sato, J. Shi, M. Z. Shou, A. Torralba, L. Torresani, M. Yan, and J. Malik. Ego4D: Around the World in 3,000 Hours of Egocentric Video. arXiv preprint arXiv:2110.07058, 2021. URL https://arxiv.org/abs/2110.07058.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2110.07058) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-79"></a>
### External [79] XIRL: Cross-embodiment Inverse Reinforcement Learning (2021)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** K. Zakka, A. Zeng, P. Florence, J. Tompson, J. Bohg, and D. Dwibedi. XIRL: Cross-embodiment Inverse Reinforcement Learning. arXiv preprint arXiv:2106.03911, 2021. URL https://arxiv.org/abs/2106.03911.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2106.03911) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-149"></a>
### External [149] The Surprising Effectiveness of Representation Learning for Visual Imitation (2021)

**Date basis:** Appendix A first public year; bibliography publication: 2022. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** J. Pari, N. M. Shafiullah, S. P. Arunachalam, and L. Pinto. The Surprising Effectiveness of Representation Learning for Visual Imitation. In Robotics: Science and Systems, 2022. URL https://www.roboticsproceedings.org/rss18/p010.pdf.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://www.roboticsproceedings.org/rss18/p010.pdf) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-236"></a>
### External [236] MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale (2021)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** D. Kalashnikov, J. Varley, Y. Chebotar, B. Swanson, R. Jonschkowski, C. Finn, S. Levine, and K. Hausman. MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale, 2021. URL https://arxiv.org/abs/2104.08212.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2104.08212) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-237"></a>
### External [237] Bridge Data: Boosting Generalization of Robotic Skills with Cross-Domain Datasets (2021)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** F. Ebert, Y. Yang, K. Schmeckpeper, B. Bucher, G. Georgakis, K. Daniilidis, C. Finn, and S. Levine. Bridge Data: Boosting Generalization of Robotic Skills with Cross-Domain Datasets, 2021. URL https://arxiv.org/abs/2109.13396.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2109.13396) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-269"></a>
### External [269] ThriftyDAgger: Budget-Aware Novelty and Risk Gating for Interactive Imitation Learning (2021)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** R. Hoque, A. Balakrishna, E. Novoseller, A. Wilcox, D. S. Brown, and K. Goldberg. ThriftyDAgger: Budget-Aware Novelty and Risk Gating for Interactive Imitation Learning, 2021. URL https://arxiv.org/abs/2109.08273.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/2109.08273) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-318"></a>
### External [318] An explanation of in-context learning as implicit Bayesian inference (2021)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** S. M. Xie, A. Raghunathan, P. Liang, and T. Ma. An explanation of in-context learning as implicit Bayesian inference. arXiv preprint arXiv:2111.02080, 2021. URL https://arxiv.org/abs/2111.02080.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2111.02080) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-32"></a>
### External [32] FlowControl: Optical Flow Based Visual Servoing (2020)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 78](https://arxiv.org/pdf/2609.36012v1#page=78).

**Citation:** M. Argus, L. Hermann, J. Long, and T. Brox. FlowControl: Optical Flow Based Visual Servoing. In IEEE/RSJ International Conference on Intelligent Robots and Systems, 2020. URL https://arxiv.org/abs/2007.00291.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Geometric demonstration transfer.

**Source URL:** [paper or source](https://arxiv.org/abs/2007.00291) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-69"></a>
### External [69] Rescaling Egocentric Vision (2020)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79).

**Citation:** D. Damen, H. Doughty, G. M. Farinella, A. Furnari, E. Kazakos, J. Ma, D. Moltisanti, J. Munro, T. Perrett, W. Price, and M. Wray. Rescaling Egocentric Vision. arXiv preprint arXiv:2006.13256, 2020. URL https://arxiv.org/abs/2006.13256.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/2006.13256) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-121"></a>
### External [121] Language models are few-shot learners (2020)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei. Language models are few-shot learners. arXiv preprint arXiv:2005.14165, 2020. URL https://arxiv.org/abs/2005.14165.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/2005.14165) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-123"></a>
### External [123] Recent Advances in Robot Learning from Demonstration (2020)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** H. Ravichandar, A. S. Polydoros, S. Chernova, and A. Billard. Recent Advances in Robot Learning from Demonstration. Annual Review of Control, Robotics, and Autonomous Systems, 2020. doi: 10.1146/annurev-control-100819-063206. URL https://www.annualreviews.org/content/journals/10.1146/annurev-control-100819-063206.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://www.annualreviews.org/content/journals/10.1146/annurev-control-100819-063206) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-158"></a>
### External [158] Transformers for One-Shot Visual Imitation (2020)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** S. Dasari and A. Gupta. Transformers for One-Shot Visual Imitation. arXiv preprint arXiv:2011.05970, 2020. URL https://arxiv.org/abs/2011.05970.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2011.05970) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-196"></a>
### External [196] FOCAL: Efficient Fully-Offline Meta-Reinforcement Learning via Distance Metric Learning and Behavior Regularization (2020)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** L. Li, R. Yang, and D. Luo. FOCAL: Efficient Fully-Offline Meta-Reinforcement Learning via Distance Metric Learning and Behavior Regularization. arXiv preprint arXiv:2010.01112, 2020. URL https://arxiv.org/abs/2010.01112.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2010.01112) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-297"></a>
### External [297] Modeling Task Uncertainty for Safe Meta-Imitation Learning (2020)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** T. Matsushima, N. Kondo, Y. Iwasawa, K. Nasuno, and Y. Matsuo. Modeling Task Uncertainty for Safe Meta-Imitation Learning. Frontiers in Robotics and AI, 7:606361, 2020. doi: 10.3389/frobt.2020.606361. URL https://doi.org/10.3389/frobt.2020.606361.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://doi.org/10.3389/frobt.2020.606361) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-300"></a>
### External [300] MetaCURE: Meta Reinforcement Learning with Empowerment-Driven Exploration (2020)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** J. Zhang, J. Wang, H. Hu, T. Chen, Y. Chen, C. Fan, and C. Zhang. MetaCURE: Meta Reinforcement Learning with Empowerment-Driven Exploration. arXiv preprint arXiv:2006.08170, 2020. URL https://arxiv.org/abs/2006.08170.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/2006.08170) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-357"></a>
### External [357] Path-Following Navigation Network Using Sparse Visual Memory (2020)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** H. Yoo, N. Kim, J. Park, and S. Oh. Path-Following Navigation Network Using Sparse Visual Memory. In 2020 20th International Conference on Control, Automation and Systems (ICCAS), pages 883–886. IEEE, October 2020. doi: 10.23919/iccas50221.2020.9268247. URL http://dx.doi.org/10.23919/ICCAS50221.2020.9268247.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](http://dx.doi.org/10.23919/ICCAS50221.2020.9268247) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-4"></a>
### External [4] Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context Variables (2019)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 76](https://arxiv.org/pdf/2609.36012v1#page=76).

**Citation:** K. Rakelly, A. Zhou, D. Quillen, C. Finn, and S. Levine. Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context Variables. arXiv preprint arXiv:1903.08254, 2019. URL https://arxiv.org/abs/1903.08254.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1903.08254) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-143"></a>
### External [143] Continual Learning for Robotics: Definition, Framework, Learning Strategies, Opportunities and Challenges (2019)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** T. Lesort, V. Lomonaco, A. Stoian, D. Maltoni, D. Filliat, and N. Díaz-Rodríguez. Continual Learning for Robotics: Definition, Framework, Learning Strategies, Opportunities and Challenges, 2019. URL https://arxiv.org/abs/1907.00182.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/1907.00182) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-147"></a>
### External [147] Watch, Try, Learn: Meta-Learning from Demonstrations and Reward (2019)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** A. Zhou, E. Jang, D. Kappler, A. Herzog, M. Khansari, P. Wohlhart, Y. Bai, M. Kalakrishnan, S. Levine, and C. Finn. Watch, Try, Learn: Meta-Learning from Demonstrations and Reward. arXiv preprint arXiv:1906.03352, 2019. URL https://arxiv.org/abs/1906.03352.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1906.03352) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-227"></a>
### External [227] RLBench: The Robot Learning Benchmark &amp; Learning Environment (2019)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** S. James, Z. Ma, D. R. Arrojo, and A. J. Davison. RLBench: The Robot Learning Benchmark &amp; Learning Environment. arXiv preprint arXiv:1909.12271, 2019. URL https://arxiv.org/abs/1909.12271.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/1909.12271) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-234"></a>
### External [234] Causal Confusion in Imitation Learning (2019)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** P. de Haan, D. Jayaraman, and S. Levine. Causal Confusion in Imitation Learning. In Advances in Neural Information Processing Systems, volume 32, 2019. URL https://papers.neurips.cc/paper\_files/paper/2019/hash/947018640bf36a2bb609d3557a285329-Abstract.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://papers.neurips.cc/paper_files/paper/2019/hash/947018640bf36a2bb609d3557a285329-Abstract.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-260"></a>
### External [260] Learning One-Shot Imitation from Humans without Humans (2019)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** A. Bonardi, S. James, and A. J. Davison. Learning One-Shot Imitation from Humans without Humans. arXiv preprint arXiv:1911.01103, 2019. URL https://arxiv.org/abs/1911.01103.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1911.01103) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-311"></a>
### External [311] Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning (2019)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** T. Yu, D. Quillen, Z. He, R. Julian, A. Narayan, H. Shively, A. Bellathur, K. Hausman, C. Finn, and S. Levine. Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning. arXiv preprint arXiv:1910.10897, 2019. URL https://arxiv.org/abs/1910.10897.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/1910.10897) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-334"></a>
### External [334] VariBAD: A Very Good Method for Bayes-Adaptive Deep RL via Meta-Learning (2019)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 92](https://arxiv.org/pdf/2609.36012v1#page=92).

**Citation:** L. Zintgraf, K. Shiarlis, M. Igl, S. Schulze, Y. Gal, K. Hofmann, and S. Whiteson. VariBAD: A Very Good Method for Bayes-Adaptive Deep RL via Meta-Learning, 2019. URL https://arxiv.org/abs/1910.08348.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1910.08348) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-8"></a>
### External [8] One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning (2018)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 76](https://arxiv.org/pdf/2609.36012v1#page=76).

**Citation:** T. Yu, C. Finn, A. Xie, S. Dasari, T. Zhang, P. Abbeel, et al. One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning. arXiv preprint arXiv:1802.01557, 2018. URL https://arxiv.org/abs/1802.01557.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1802.01557) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-140"></a>
### External [140] QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation (2018)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** D. Kalashnikov, A. Irpan, P. Pastor, J. Ibarz, A. Herzog, E. Jang, D. Quillen, E. Holly, M. Kalakrishnan, V. Vanhoucke, and S. Levine. QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation. arXiv preprint arXiv:1806.10293, 2018. URL https://arxiv.org/abs/1806.10293.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/1806.10293) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-157"></a>
### External [157] Task-Embedded Control Networks for Few-Shot Imitation Learning (2018)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** S. James, M. Bloesch, and A. J. Davison. Task-Embedded Control Networks for Few-Shot Imitation Learning. arXiv preprint arXiv:1810.03237, 2018. URL https://arxiv.org/abs/1810.03237.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1810.03237) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-167"></a>
### External [167] Behavioral Cloning from Observation (2018)

**Date basis:** Bibliography year. **Bibliography:** [p. 84](https://arxiv.org/pdf/2609.36012v1#page=84).

**Citation:** F. Torabi, G. Warnell, and P. Stone. Behavioral Cloning from Observation. arXiv preprint arXiv:1805.01954, 2018. URL https://arxiv.org/abs/1805.01954.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/1805.01954) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-179"></a>
### External [179] Universal Planning Networks (2018)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** A. Srinivas, A. Jabri, P. Abbeel, S. Levine, and C. Finn. Universal Planning Networks. arXiv preprint arXiv:1804.00645, 2018. URL https://arxiv.org/abs/1804.00645.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://arxiv.org/abs/1804.00645) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-294"></a>
### External [294] Robustness via Retrying: Closed-Loop Robotic Manipulation with Self-Supervised Learning (2018)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 90](https://arxiv.org/pdf/2609.36012v1#page=90).

**Citation:** F. Ebert, S. Dasari, A. X. Lee, S. Levine, and C. Finn. Robustness via Retrying: Closed-Loop Robotic Manipulation with Self-Supervised Learning. In Conference on Robot Learning, 2018. URL https://proceedings.mlr.press/v87/ebert18a.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** World-model-based control.

**Source URL:** [paper or source](https://proceedings.mlr.press/v87/ebert18a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-354"></a>
### External [354] On Evaluation of Embodied Navigation Agents (2018)

**Date basis:** Bibliography year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** P. Anderson, A. Chang, D. S. Chaplot, A. Dosovitskiy, S. Gupta, V. Koltun, J. Kosecka, J. Malik, R. Mottaghi, M. Savva, and A. R. Zamir. On Evaluation of Embodied Navigation Agents, 2018. URL https://arxiv.org/abs/1807.06757.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Evaluation.

**Source URL:** [paper or source](https://arxiv.org/abs/1807.06757) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-355"></a>
### External [355] Zero-Shot Visual Imitation (2018)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** D. Pathak, P. Mahmoudieh, G. Luo, P. Agrawal, D. Chen, Y. Shentu, E. Shelhamer, J. Malik, A. A. Efros, and T. Darrell. Zero-Shot Visual Imitation. In ICLR, 2018. URL https://arxiv.org/abs/1804.08606.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1804.08606) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="visual-memory-2018"></a>
### External [356] Visual Memory for Robust Path Following (2018)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** A. Kumar, S. Gupta, D. Fouhey, S. Levine, and J. Malik. Visual Memory for Robust Path Following. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 31. Curran Associates, Inc., 2018. URL https://proceedings.neurips.cc/paper\_files/paper/2018/file/66368270ffd51418ec58bd793f2d9b1b-Paper.pdf.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://proceedings.neurips.cc/paper_files/paper/2018/file/66368270ffd51418ec58bd793f2d9b1b-Paper.pdf) — transcribed from the external survey.

**Reading-note evidence:** [p. 19](https://arxiv.org/pdf/2609.36012v1#page=19), [p. 42](https://arxiv.org/pdf/2609.36012v1#page=42), [p. 57](https://arxiv.org/pdf/2609.36012v1#page=57).

- **Deployment context:** ordered views and recorded actions from a demonstrated route
- **Action mechanism:** encodes an action-bearing path memory that guides execution under noise and scene changes
- **Deployment weights:** not detailed in the cited survey passages
- **Setting discussed:** route following under motion noise and scene changes
- **Survey evidence:** The survey contrasts RPF’s action-bearing route memory with visual subgoals and with environment previews for new navigation goals.
- **Why read it:** Makes the difference between following a taught route and learning reusable scene knowledge explicit.
- **Adaptation target:** demonstrated route
- **Evidence description:** navigation method discussion
- **Interpretation limit:** A route recording prescribes a path; it does not by itself establish general navigation knowledge for arbitrary new goals.

<a id="ref-358"></a>
### External [358] Semi-parametric topological memory for navigation (2018)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 93](https://arxiv.org/pdf/2609.36012v1#page=93).

**Citation:** N. Savinov, A. Dosovitskiy, and V. Koltun. Semi-parametric topological memory for navigation. In International Conference on Learning Representations (ICLR), 2018. URL https://arxiv.org/abs/1803.00653.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/1803.00653) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="one-shot-imitation-2017"></a>
### External [1] One-Shot Imitation Learning (2017)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 76](https://arxiv.org/pdf/2609.36012v1#page=76).

**Citation:** Y. Duan, M. Andrychowicz, B. C. Stadie, J. Ho, J. Schneider, I. Sutskever, et al. One-Shot Imitation Learning. arXiv preprint arXiv:1703.07326, 2017. URL https://arxiv.org/abs/1703.07326.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1703.07326) — transcribed from the external survey.

**Reading-note evidence:** [p. 12](https://arxiv.org/pdf/2609.36012v1#page=12), [p. 41](https://arxiv.org/pdf/2609.36012v1#page=41), [p. 47](https://arxiv.org/pdf/2609.36012v1#page=47).

- **Deployment context:** one support demonstration specifying the behavior of a paired query execution
- **Action mechanism:** paired-execution training teaches a contextual policy to infer query actions from a support episode
- **Deployment weights:** fixed contextual deployment
- **Setting discussed:** early task-family adaptation and support–query training
- **Survey evidence:** The survey identifies this work as an early paired-execution principle: one task instance teaches how to act in another.
- **Why read it:** Provides the training principle underlying later demonstration-conditioned policies.
- **Adaptation target:** another instance of the demonstrated task
- **Evidence description:** historical and training-method discussion
- **Context amount:** 1 support demonstration
- **Interpretation limit:** The survey describes adaptation within a trained task family; the cited discussion does not establish broad cross-embodiment transfer.

<a id="ref-3"></a>
### External [3] A Simple Neural Attentive Meta-Learner (2017)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 76](https://arxiv.org/pdf/2609.36012v1#page=76).

**Citation:** N. Mishra, M. Rohaninejad, X. Chen, and P. Abbeel. A Simple Neural Attentive Meta-Learner. arXiv preprint arXiv:1707.03141, 2017. URL https://arxiv.org/abs/1707.03141.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1707.03141) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-7"></a>
### External [7] One-Shot Visual Imitation Learning via Meta-Learning (2017)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 76](https://arxiv.org/pdf/2609.36012v1#page=76).

**Citation:** C. Finn, T. Yu, T. Zhang, P. Abbeel, and S. Levine. One-Shot Visual Imitation Learning via Meta-Learning. arXiv preprint arXiv:1709.04905, 2017. URL https://arxiv.org/abs/1709.04905.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1709.04905) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-26"></a>
### External [26] Neural Task Programming: Learning to Generalize Across Hierarchical Tasks (2017)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 77](https://arxiv.org/pdf/2609.36012v1#page=77).

**Citation:** D. Xu, S. Nair, Y. Zhu, J. Gao, A. Garg, L. Fei-Fei, and S. Savarese. Neural Task Programming: Learning to Generalize Across Hierarchical Tasks. arXiv preprint arXiv:1710.01813, 2017. URL https://arxiv.org/abs/1710.01813.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Skill- and agent-based execution.

**Source URL:** [paper or source](https://arxiv.org/abs/1710.01813) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-71"></a>
### External [71] The "something something" video database for learning and evaluating visual common sense (2017)

**Date basis:** Bibliography year. **Bibliography:** [p. 79](https://arxiv.org/pdf/2609.36012v1#page=79), [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** R. Goyal, S. E. Kahou, V. Michalski, J. Materzyńska, S. Westphal, H. Kim, V. Haenel, I. Fruend, P. Yianilos, M. Mueller-Freitag, F. Hoppe, C. Thurau, I. Bax, and R. Memisevic. The "something something" video database for learning and evaluating visual common sense. arXiv preprint arXiv:1706.04261, 2017. URL https://arxiv.org/abs/1706.04261.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Data resources.

**Source URL:** [paper or source](https://arxiv.org/abs/1706.04261) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-78"></a>
### External [78] Time-Contrastive Networks: Self-Supervised Learning from Video (2017)

**Date basis:** Bibliography year. **Bibliography:** [p. 80](https://arxiv.org/pdf/2609.36012v1#page=80).

**Citation:** P. Sermanet, C. Lynch, Y. Chebotar, J. Hsu, E. Jang, S. Schaal, and S. Levine. Time-Contrastive Networks: Self-Supervised Learning from Video. arXiv preprint arXiv:1704.06888, 2017. URL https://arxiv.org/abs/1704.06888.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/1704.06888) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-146"></a>
### External [146] Preparing for the Unknown: Learning a Universal Policy with Online System Identification (2017)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** W. Yu, J. Tan, C. K. Liu, and G. Turk. Preparing for the Unknown: Learning a Universal Policy with Online System Identification. arXiv preprint arXiv:1702.02453, 2017. URL https://arxiv.org/abs/1702.02453.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1702.02453) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-231"></a>
### External [231] Attention is all you need (2017)

**Date basis:** Bibliography year. **Bibliography:** [p. 87](https://arxiv.org/pdf/2609.36012v1#page=87).

**Citation:** A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. In Advances in Neural Information Processing Systems, volume 30, 2017. URL https://arxiv.org/abs/1706.03762.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://arxiv.org/abs/1706.03762) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-268"></a>
### External [268] DART: Noise Injection for Robust Imitation Learning (2017)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** M. Laskey, J. Lee, R. Fox, A. Dragan, and K. Goldberg. DART: Noise Injection for Robust Imitation Learning, 2017. URL https://arxiv.org/abs/1703.09327.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/1703.09327) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-2"></a>
### External [2] RL2: Fast Reinforcement Learning via Slow Reinforcement Learning (2016)

**Date basis:** Appendix A first public year. **Bibliography:** [p. 76](https://arxiv.org/pdf/2609.36012v1#page=76).

**Citation:** Y. Duan, J. Schulman, X. Chen, P. L. Bartlett, I. Sutskever, and P. Abbeel. RL2: Fast Reinforcement Learning via Slow Reinforcement Learning. arXiv preprint arXiv:1611.02779, 2016. URL https://arxiv.org/abs/1611.02779.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Context-conditioned policies.

**Source URL:** [paper or source](https://arxiv.org/abs/1611.02779) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-139"></a>
### External [139] End-to-End Training of Deep Visuomotor Policies (2015)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** S. Levine, C. Finn, T. Darrell, and P. Abbeel. End-to-End Training of Deep Visuomotor Policies. arXiv preprint arXiv:1504.00702, 2015. URL https://arxiv.org/abs/1504.00702.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://arxiv.org/abs/1504.00702) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-138"></a>
### External [138] Towards a Unified Behavior Trees Framework for Robot Control (2014)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** A. Marzinotto, M. Colledanchise, C. Smith, and P. Ögren. Towards a Unified Behavior Trees Framework for Robot Control. In IEEE International Conference on Robotics and Automation, 2014. URL https://www.csc.kth.se/~ccs/Publications/icra14b.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://www.csc.kth.se/~ccs/Publications/icra14b.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-301"></a>
### External [301] Designing Robot Learners that Ask Good Questions (2012)

**Date basis:** Bibliography year. **Bibliography:** [p. 91](https://arxiv.org/pdf/2609.36012v1#page=91).

**Citation:** M. Cakmak and A. L. Thomaz. Designing Robot Learners that Ask Good Questions. In ACM/IEEE International Conference on Human-Robot Interaction, 2012. URL https://homes.cs.washington.edu/~mcakmak/pdfs/2012/cakmak2012hri.pdf.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://homes.cs.washington.edu/~mcakmak/pdfs/2012/cakmak2012hri.pdf) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-137"></a>
### External [137] Hierarchical Task and Motion Planning in the Now (2011)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** L. P. Kaelbling and T. Lozano-Pérez. Hierarchical Task and Motion Planning in the Now. In IEEE International Conference on Robotics and Automation, pages 1470–1477, 2011. doi: 10.1109/ICRA.2011.5980391. URL https://people.csail.mit.edu/tlp/pdf/2011/hpnICRA11Final.pdf.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://people.csail.mit.edu/tlp/pdf/2011/hpnICRA11Final.pdf) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-267"></a>
### External [267] A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (2011)

**Date basis:** Bibliography year. **Bibliography:** [p. 89](https://arxiv.org/pdf/2609.36012v1#page=89).

**Citation:** S. Ross, G. J. Gordon, and J. A. Bagnell. A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. In Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics, volume 15, pages 627–635, 2011. URL https://proceedings.mlr.press/v15/ross11a.html.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Training and representations.

**Source URL:** [paper or source](https://proceedings.mlr.press/v15/ross11a.html) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-122"></a>
### External [122] A Survey of Robot Learning from Demonstration (2009)

**Date basis:** Bibliography year. **Bibliography:** [p. 82](https://arxiv.org/pdf/2609.36012v1#page=82).

**Citation:** B. D. Argall, S. Chernova, M. Veloso, and B. Browning. A Survey of Robot Learning from Demonstration. Robotics and Autonomous Systems, 2009. doi: 10.1016/j.robot.2008.10.024. URL https://publications.ri.cmu.edu/a-survey-of-robot-learning-from-demonstration.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://publications.ri.cmu.edu/a-survey-of-robot-learning-from-demonstration) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-194"></a>
### External [194] Visual servo control, part i: Basic approaches (2006)

**Date basis:** Bibliography year. **Bibliography:** [p. 85](https://arxiv.org/pdf/2609.36012v1#page=85).

**Citation:** F. Chaumette and S. Hutchinson. Visual servo control, part i: Basic approaches. IEEE Robotics &amp; Automation Magazine, 13(4):82–90, 2006. doi: 10.1109/MRA.2006.250573. URL https://web.mit.edu/amcp/OldFiles/drg/Chaumette\_Part\_I.pdf.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://web.mit.edu/amcp/OldFiles/drg/Chaumette_Part_I.pdf) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-136"></a>
### External [136] A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation (1987)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** O. Khatib. A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation. IEEE Journal on Robotics and Automation, 3(1):43–53, 1987. doi: 10.1109/JRA.1987.1087068. URL https://khatib.stanford.edu/publications/pdfs/Khatib\_1987\_RA.pdf.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://khatib.stanford.edu/publications/pdfs/Khatib_1987_RA.pdf) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-135"></a>
### External [135] A Robust Layered Control System for a Mobile Robot (1985)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** R. A. Brooks. A Robust Layered Control System for a Mobile Robot. Technical Report A.I. Memo 864, Massachusetts Institute of Technology, Artificial Intelligence Laboratory, 1985. URL https://people.csail.mit.edu/brooks/papers/AIM-864.pdf.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://people.csail.mit.edu/brooks/papers/AIM-864.pdf) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.

<a id="ref-134"></a>
### External [134] STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving (1971)

**Date basis:** Bibliography year. **Bibliography:** [p. 83](https://arxiv.org/pdf/2609.36012v1#page=83).

**Citation:** R. E. Fikes and N. J. Nilsson. STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving. Artificial Intelligence, 2(3–4):189–208, 1971. doi: 10.1016/0004-3702(71)90010-5. URL https://www.sciencedirect.com/science/article/pii/0004370271900105.

**Our framework:** Mapping pending; this reference is retained in the full collection.

**External survey group:** Foundations and surveys.

**Source URL:** [paper or source](https://www.sciencedirect.com/science/article/pii/0004370271900105) — transcribed from the external survey.

**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated.
