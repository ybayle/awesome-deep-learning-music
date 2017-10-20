# Deep Learning for Music (DL4M) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

The role of this curated list is to gather scientific articles, thesis and reports that use deep learning approaches applied to music.
The list is currently under construction but feel free to contribute to the missing fields and to add other resources.
The resources provided here come from my review of the state-of-the-art for my PhD Thesis for which an article is being written.
There are already surveys on deep learning for [music generation](https://arxiv.org/pdf/1709.01620.pdf), [speech separation](https://arxiv.org/ftp/arxiv/papers/1708/1708.07524.pdf) and [speaker identification](https://www.researchgate.net/profile/Seyed_Reza_Shahamiri/publication/319158024_Speaker_Identification_Features_Extraction_Methods_A_Systematic_Review/links/599e2816aca272dff12fdef1/Speaker-Identification-Features-Extraction-Methods-A-Systematic-Review.pdf).
However, these surveys do not cover music information retrieval tasks that are included in this repository.

## Table of contents

- [DL4M summary](#dl4m-summary)
- [DL4M details](#dl4m-details)
- [Code without articles](#code-without-articles)
- [Statistics and visualisations](#statistics-and-visualisations)
- [How To Contribute](#how-to-contribute)
- [FAQ](#faq)
- [Acronyms used](#acronyms-used)
- [Sources](#sources)
- [Contributors](#contributors)
- [Other useful related lists](#other-useful-related-lists)

## DL4M summary 

|  Articles, Thesis and Reports | Code |
|-------------------------------|------|
| [An efficient approach for segmentation, feature extraction and classification of audio signals](http://file.scirp.org/pdf/CS_2016042615054817.pdf) | No |
| [Gabor frames and deep scattering networks in audio processing](https://arxiv.org/pdf/1706.08818.pdf) | No |
| [Vision-based detection of acoustic timed events: A case study on clarinet note onsets](http://dorienherremans.com/dlm2017/papers/bazzica2017clarinet.pdf) | No |
| Neural net modeling of music | No |
| [Deep learning techniques for music generation - A survey](https://arxiv.org/pdf/1709.01620.pdf) | No |
| [A supervised learning approach to musical style recognition](https://www.researchgate.net/profile/Giuseppe_Buzzanca/publication/228588086_A_supervised_learning_approach_to_musical_style_recognition/links/54b43ee90cf26833efd0109f.pdf) | No |
| [XFlow: 1D <-> 2D cross-modal deep neural networks for audiovisual classification](https://arxiv.org/pdf/1709.00572.pdf) | No |
| [Machine listening intelligence](http://dorienherremans.com/dlm2017/papers/cella2017mli.pdf) | No |
| [Deep multimodal network for multi-label classification](http://ieeexplore.ieee.org/abstract/document/8019322/) | No |
| [A tutorial on deep learning for music information retrieval](https://arxiv.org/pdf/1709.04396.pdf) | [GitHub](https://github.com/keunwoochoi/dl4mir) |
| [A comparison on audio signal preprocessing methods for deep neural networks on music tagging](https://arxiv.org/pdf/1709.01922.pdf) | [GitHub](https://github.com/keunwoochoi/transfer_learning_music) |
| [Text-based LSTM networks for automatic music composition](https://drive.google.com/file/d/0B1OooSxEtl0FcG9MYnY2Ylh5c0U/view) | No |
| [Towards playlist generation algorithms using RNNs trained on within-track transitions](https://arxiv.org/pdf/1606.02096.pdf) | No |
| [Automatic tagging using deep convolutional neural networks](https://arxiv.org/pdf/1606.00298.pdf) | No |
| [Transfer learning for music classification and regression tasks](https://arxiv.org/pdf/1703.09179v3.pdf) | [GitHub](https://github.com/keunwoochoi/transfer_learning_music) |
| [Convolutional recurrent neural networks for music classification](http://ieeexplore.ieee.org/abstract/document/7952585/) | [GitHub](https://github.com/keunwoochoi/icassp_2017) |
| [Auralisation of deep convolutional neural networks: Listening to learned features](http://ismir2015.uma.es/LBD/LBD24.pdf) | No |
| [An evaluation of convolutional neural networks for music classification using spectrograms](http://www.inf.ufpr.br/lesoliveira/download/ASOC2017.pdf) | No |
| [The munich LSTM-RNN approach to the MediaEval 2014 "Emotion in music" task](https://pdfs.semanticscholar.org/8a24/c5131d5a28165f719697028c34b00e6d3f60.pdf) | No |
| [A machine learning approach to musical style recognition](http://repository.cmu.edu/cgi/viewcontent.cgi?article=1496&context=compsci) | No |
| [Automatic chord estimation on seventhsbass chord vocabulary using deep neural network](http://ieeexplore.ieee.org/abstract/document/7471677/) | No |
| [Large vocabulary automatic chord estimation using deep neural nets: Design framework, system variations and limitations](https://arxiv.org/pdf/1709.07153.pdf) | No |
| [Audio-based music classification with a pretrained convolutional network](http://www.ismir2011.ismir.net/papers/PS6-3.pdf) | No |
| [Multiscale approaches to music audio feature learning](http://ismir2013.ismir.net/wp-content/uploads/2013/09/69_Paper.pdf) | No |
| [End-to-end learning for music audio](http://ieeexplore.ieee.org/abstract/document/6854950/) | No |
| [Basic filters for convolutional neural networks: Training or design?](https://arxiv.org/pdf/1709.02291.pdf) | No |
| [Ensemble Of Deep Neural Networks For Acoustic Scene Classification](https://arxiv.org/pdf/1708.05826.pdf) | No |
| [Robust downbeat tracking using an ensemble of convolutional networks](http://ieeexplore.ieee.org/abstract/document/7728057/) | No |
| [Downbeat tracking with multiple features and deep neural networks](http://perso.telecom-paristech.fr/~grichard/Publications/2015-durand-icassp.pdf) | No |
| [Music signal processing using vector product neural networks](http://dorienherremans.com/dlm2017/papers/fan2017vector.pdf) | No |
| [Deep learning for music genre classification](https://courses.engr.illinois.edu/ece544na/fa2014/Tao_Feng.pdf) | No |
| [Multi-phase learning for jazz improvisation and interaction](http://www.cs.smith.edu/~jfrankli/papers/CtColl01.pdf) | No |
| [Recognition of acoustic events using deep neural networks](https://www.cs.tut.fi/sgn/arg/music/tuomasv/dnn_eusipco2014.pdf) | No |
| [Transforming musical signals through a genre classifying convolutional neural network](http://dorienherremans.com/dlm2017/papers/geng2017genre.pdf) | No |
| [Audio to score matching by combining phonetic and duration information](https://arxiv.org/pdf/1707.03547.pdf) | [GitHub](https://github.com/ronggong/jingjuSingingPhraseMatching/tree/v0.1.0) |
| [Musical networks: Parallel distributed perception and performance](https://s3.amazonaws.com/academia.edu.documents/3551783/10.1.1.39.6248.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1507055806&Signature=5mGzQc7bvJgUZYfXOmCX8eeNQOs%3D&response-content-disposition=inline%3B%20filename%3DMusical_networks_Parallel_distributed_pe.pdf) | No |
| [Music boundary detection using neural networks on spectrograms and self-similarity lag matrices](http://www.ofai.at/~jan.schlueter/pubs/2015_eusipco.pdf) | No |
| [Deep image features in music information retrieval](https://www.degruyter.com/downloadpdf/j/eletel.2014.60.issue-4/eletel-2014-0042/eletel-2014-0042.pdf) | No |
| [Interactive music generation with positional constraints using anticipation-RNNs](https://arxiv.org/pdf/1709.06404.pdf) | No |
| [Deep rank-based transposition-invariant distances on musical sequences](https://arxiv.org/pdf/1709.00740.pdf) | No |
| [GLSR-VAE: Geodesic latent space regularization for variational autoencoder architectures](https://arxiv.org/pdf/1707.04588.pdf) | No |
| [DeepBach: A steerable model for Bach chorales generation](https://arxiv.org/pdf/1612.01010.pdf) | [GitHub](https://github.com/Ghadjeres/DeepBach) |
| [Deep convolutional neural networks for predominant instrument recognition in polyphonic music](http://dl.acm.org/citation.cfm?id=3068697) | No |
| [CNN architectures for large-scale audio classification](https://arxiv.org/pdf/1609.09430v2.pdf) | No |
| [Classification of spatial audio location and content using convolutional neural networks](https://www.researchgate.net/profile/Toni_Hirvonen/publication/276061831_Classification_of_Spatial_Audio_Location_and_Content_Using_Convolutional_Neural_Networks/links/5550665908ae12808b37fe5a/Classification-of-Spatial-Audio-Location-and-Content-Using-Convolutional-Neural-Networks.pdf) | No |
| [Bayesian meter tracking on learned signal representations](http://www.rhythmos.org/MMILab-Andre_files/ISMIR2016_CNNDBNbeats_camready.pdf) | No |
| [DeepSheet: A sheet music generator based on deep learning](http://ieeexplore.ieee.org/abstract/document/8026272/) | No |
| [Deep learning for music](https://arxiv.org/pdf/1606.04930.pdf) | No |
| [From music audio to chord tablature: Teaching deep convolutional networks to play guitar](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202014/papers/p7024-humphrey.pdf) | No |
| [Rethinking automatic chord recognition with convolutional neural networks](http://ieeexplore.ieee.org/abstract/document/6406762/) | No |
| [Moving beyond feature design: Deep architectures and automatic feature learning in music informatics](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.294.2304&rep=rep1&type=pdf) | No |
| [Talking Drums: Generating drum grooves with neural networks](http://dorienherremans.com/dlm2017/papers/hutchings2017drums.pdf) | No |
| [Music emotion recognition via end-to-end multimodal neural networks](http://ceur-ws.org/Vol-1905/recsys2017_poster18.pdf) | No |
| [Learning temporal features using a deep neural network and its application to music genre classification](https://www.researchgate.net/profile/Il_Young_Jeong/publication/305683876_Learning_temporal_features_using_a_deep_neural_network_and_its_application_to_music_genre_classification/links/5799a27c08aec89db7bb9f92.pdf) | No |
| [On the potential of simple framewise approaches to piano transcription](https://arxiv.org/pdf/1612.05153.pdf) | No |
| [Deep learning, audio adversaries, and music content analysis](http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6905/pdf/imm6905.pdf) | No |
| [Deep learning and music adversaries](https://arxiv.org/pdf/1507.04761.pdf) | [GitHub](https://github.com/coreyker/dnn-mgr) |
| [Chord label personalization through deep learning of integrated harmonic interval-based representations](http://dorienherremans.com/dlm2017/papers/koops2017pers.pdf) | No |
| [Feature learning for chord recognition: The deep chroma extractor](https://arxiv.org/pdf/1612.05065.pdf) | [GitHub](https://github.com/fdlm/chordrec/tree/master/experiments/ismir2016) |
| [A fully convolutional deep auditory model for musical chord recognition](https://www.researchgate.net/profile/Filip_Korzeniowski/publication/305590295_A_Fully_Convolutional_Deep_Auditory_Model_for_Musical_Chord_Recognition/links/579486ba08aed51475cc6958/A-Fully-Convolutional-Deep-Auditory-Model-for-Musical-Chord-Recognition.pdf?_iepl%5BhomeFeedViewId%5D=HTzFFmKPia2YminQ4psHT5at&_iepl%5Bcontexts%5D%5B0%5D=pcfhf&_iepl%5BinteractionType%5D=publicationDownload&origin=publication_detail&ev=pub_int_prw_xdl&msrp=Dz_6LKHzYcPyP-LmgZPF-m63ayZ6k0entFEntooiu_e32zfETNQXKPQSTFOI87NONIIQuUQdnUtwORdomTXfteTrb09KiAIdDtBJnw_02P6JeRr5zu2eyaCG.2Uxsi_eENxtbYL39lvorIK8LofRYhkgpUHzpzmVzkIEiyHc0wUY87rEa4PH1qbXi4k4RyagHUsA2IsZtewnprglORjx2v9Cwbk9ZfQ.cd67BaqtHul_hE6SX6vUFKuldz81aH6dWq-cYMkq5vQKCHcvB8l9zgeM694Efb_r2wBB5GT9idt3OLeME0UxVHI6ROxamgK3LMNlSw.JtZXAo9HhR9t-8Wl3gxJgnoM4--rtmDEUDbXSWezbFyU-CoB_nyfxbRQ4kdoN4-5aJ3Tgx4YHdikicqAhc_cezB2ZntjxkB4rEDx1A) | No |
| [End-to-end musical key estimation using a convolutional neural network](https://arxiv.org/pdf/1706.02921.pdf) | No |
| [MediaEval 2017 AcousticBrainz genre task: Multilayer perceptron approach](http://www.cp.jku.at/research/papers/Koutini_2017_mediaeval-acousticbrainz.pdf) | No |
| [The representation of pitch in a neural net model of chord classification](http://www.jstor.org/stable/3679550) | No |
| [Unsupervised feature learning for audio classification using convolutional deep belief networks](http://papers.nips.cc/paper/3674-unsupervised-feature-learning-for-audio-classification-using-convolutional-deep-belief-networks.pdf) | No |
| [Multi-level and multi-scale feature aggregation using pre-trained convolutional neural networks for music auto-tagging](https://arxiv.org/pdf/1703.01793v2.pdf) | No |
| [Multi-level and multi-scale feature aggregation using sample-level deep convolutional neural networks for music classification](https://arxiv.org/pdf/1706.06810.pdf) | [GitHub](https://github.com/jongpillee/musicTagging_MSD) |
| [Sample-level deep convolutional neural networks for music auto-tagging using raw waveforms](https://arxiv.org/pdf/1703.01789v2.pdf) | No |
| [Singing voice detection with deep recurrent neural networks](https://hal-imt.archives-ouvertes.fr/hal-01110035/) | No |
| [Creation by refinement: A creativity paradigm for gradient descent learning networks](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=23933) | No |
| [Algorithms for music composition by neural nets: Improved CBR paradigms](https://quod.lib.umich.edu/cgi/p/pod/dod-idx/algorithms-for-music-composition.pdf?c=icmc;idno=bbp2372.1989.044;format=pdf) | No |
| [Audio musical genre classification using convolutional neural networks and pitch and tempo transformations](http://lbms03.cityu.edu.hk/theses/c_ftt/mphil-cs-b39478026f.pdf) | No |
| [Automatic instrument recognition in polyphonic music using convolutional neural networks](https://arxiv.org/pdf/1511.05520.pdf) | No |
| [Automatic musical pattern feature extraction using convolutional neural network](https://www.researchgate.net/profile/Antoni_Chan2/publication/44260643_Automatic_Musical_Pattern_Feature_Extraction_Using_Convolutional_Neural_Network/links/02e7e523dac6bb86b0000000.pdf) | No |
| [A deep bidirectional long short-term memory based multi-scale approach for music dynamic emotion prediction](http://ieeexplore.ieee.org/document/7471734/) | No |
| [Harmonic and percussive source separation using a convolutional auto encoder](http://www.eurasip.org/Proceedings/Eusipco/Eusipco2017/papers/1570346835.pdf) | No |
| [Event localization in music auto-tagging](http://mac.citi.sinica.edu.tw/~yang/pub/liu16mm.pdf) | [GitHub](https://github.com/ciaua/clip2frame) |
| [Deep convolutional networks on the pitch spiral for musical instrument recognition](https://github.com/lostanlen/ismir2016/blob/master/paper/lostanlen_ismir2016.pdf) | [GitHub](https://github.com/lostanlen/ismir2016) |
| [A deep learning approach to source separation and remixing of hiphop music](https://repositori.upf.edu/bitstream/handle/10230/32919/Martel_2017.pdf?sequence=1&isAllowed=y) | No |
| [Neural network based model for classification of music type](http://ieeexplore.ieee.org/abstract/document/514161/) | No |
| [A software framework for musical data augmentation](https://bmcfee.github.io/papers/ismir2015_augmentation.pdf) | No |
| [Generating data to train convolutional neural networks for classical music source separation](https://www.researchgate.net/profile/Marius_Miron/publication/318322107_Generating_data_to_train_convolutional_neural_networks_for_classical_music_source_separation/links/59637cc3458515a3575b93c6/Generating-data-to-train-convolutional-neural-networks-for-classical-music-source-separation.pdf?_iepl%5BhomeFeedViewId%5D=WchoMnlUL1Hk9hBLVTeR8Amh&_iepl%5Bcontexts%5D%5B0%5D=pcfhf&_iepl%5BinteractionType%5D=publicationDownload&origin=publication_detail&ev=pub_int_prw_xdl&msrp=p3lQ8M4uZlb4TF5Hv9a2U3P2y4wW7ant5KWj4E5-OcD1Mg53p1ykTKHMG9_zVTB9n6mI8fvZOCL2Xhpru186pCEY-2ZxiYR-CB8_QvwHc1kUG-QE4SHdProR.LoJb2BDOiiQth3iR9xgZUxxCWEJgtTBF4whFrFa01OD49-3YYRxA0WQVN--zhtQU_7C2Pt0rKdwoFxT1pfxFvnKXSXmy2eT1Jpz-pw.U1QLoFO_Uc6aQVr2Nm2FcAi6BqAUfngH2Or5__6wegbCgVvTYoIGt22tmCkYbGTOQ_4PxBgt1LrvsFQiL0oMyogP8Yk8myTj0gs9jw.fGpkufGqAI4R2v8Hfe0ThcXL7M7yN2PuAlx974BGVn50SdUWvNhhIPWBD-zWTn8NKtVJx3XrjKXFrMgi9Cx7qGrNP8tBWpha6Srf6g) | [GitHub](https://github.com/MTG/DeepConvSep) |
| [Monaural score-informed source separation for classical music using convolutional neural networks](https://www.researchgate.net/profile/Marius_Miron/publication/318637038_Monaural_score-informed_source_separation_for_classical_music_using_convolutional_neural_networks/links/597327c6458515e26dfdb007/Monaural-score-informed-source-separation-for-classical-music-using-convolutional-neural-networks.pdf?_iepl%5BhomeFeedViewId%5D=WchoMnlUL1Hk9hBLVTeR8Amh&_iepl%5Bcontexts%5D%5B0%5D=pcfhf&_iepl%5BinteractionType%5D=publicationDownload&origin=publication_detail&ev=pub_int_prw_xdl&msrp=Hp6dDqMepEiRZ5E6WkreaqyjFkFkwMxPFoJvr14etVJsoKZBc5qb99fBnJjVUZrRHLFRhaXvNY9k1sMvYPOouuGbQP0YhEGm28zLw_55Zewu86WGnHck1Tqi.93HH2WqXfTedn6IaZRjjhQGYZVDHBz1X6nr4ABBgMAVv584gvGN3sW5IyBAY-4MBWf5DJFPBGm8zsaC2dKz8G-odZPfosWoXY0afAQ.KoCP2mO9l31lCER0oMZMZBrbuRGvb6ZzeBwHb88pL8AhMfJk03Hj1eLrohQIjPDETBj4hhqb0gniDGJgtZ9GnW64ZNjh9GbQDrIl5A.egNQTyC7t8P26zCQWrbEhf51Pxy2JRBZoTkH6SpRHHhRhFl1_AT_AT481lMcFI34-JbeRq-5oTQR7DpvAuw7iUIivd78ltuxpI9syg) | [GitHub](https://github.com/MTG/DeepConvSep) |
| [Neural network music composition by prediction: Exploring the benefits of psychoacoustic constraints and multi-scale processing](http://www-labs.iro.umontreal.ca/~pift6080/H09/documents/papers/mozer-music.pdf) | No |
| [Local-feature-map integration using convolutional neural networks for music genre classification](http://liris.cnrs.fr/Documents/Liris-5602.pdf) | No |
| [A deep bag-of-features model for music auto-tagging](https://arxiv.org/pdf/1508.04999v1.pdf) | No |
| [Learning sparse feature representations for music annotation and retrieval](https://pdfs.semanticscholar.org/099d/85f25e9336f48ff64287a4b53ee5fb64ab51.pdf) | No |
| [A convolutional-kernel based approach for note onset detection in piano-solo audio signals](http://www.murase.nuie.nagoya-u.ac.jp/~ide/res/paper/E04-conference-pablo-1.pdf) | No |
| [Multi-label music genre classification from audio, text, and images using deep features](https://arxiv.org/abs/1707.04916) | [GitHub](https://github.com/sergiooramas/tartarus) |
| [A deep multimodal approach for cold-start music recommendation](https://arxiv.org/pdf/1706.09739.pdf) | [GitHub](https://github.com/sergiooramas/tartarus) |
| [Melody extraction and detection through LSTM-RNN with harmonic sum loss](http://ieeexplore.ieee.org/abstract/document/7952660/) | No |
| [Representation learning of music using artist labels](https://arxiv.org/pdf/1710.06648.pdf) | No |
| [Music-noise segmentation in spectrotemporal domain using convolutional neural networks](http://ismir2015.uma.es/LBD/LBD27.pdf) | No |
| [Musical instrument sound classification with deep convolutional neural network using feature fusion approach](https://arxiv.org/ftp/arxiv/papers/1512/1512.07370.pdf) | No |
| [Toward inverse control of physics-based sound synthesis](http://dorienherremans.com/dlm2017/papers/pfalz2017synthesis.pdf) | [Website](https://www.cct.lsu.edu/~apfalz/inverse_control.html) |
| [Robust audio event recognition with 1-max pooling convolutional neural networks](https://arxiv.org/pdf/1604.06338.pdf) | No |
| [DNN and CNN with weighted and multi-task loss functions for audio event detection](https://arxiv.org/pdf/1708.03211.pdf) | No |
| [Environmental sound classification with convolutional neural networks](http://karol.piczak.com/papers/Piczak2015-ESC-ConvNet.pdf) | No |
| [Score-informed syllable segmentation for a cappella singing voice with convolutional neural networks](https://arxiv.org/pdf/1707.03544.pdf) | [GitHub](https://github.com/ronggong/jingjuSyllabicSegmentaion/tree/v0.1.0) |
| [Experimenting with musically motivated convolutional neural networks](http://jordipons.me/media/CBMI16.pdf) | [GitHub](https://github.com/jordipons/) |
| [Designing efficient architectures for modeling temporal features with convolutional neural networks](http://ieeexplore.ieee.org/document/7952601/) | [GitHub](https://github.com/jordipons/ICASSP2017) |
| [Timbre analysis of music audio signals with convolutional neural networks](https://github.com/ronggong/EUSIPCO2017) | [GitHub](https://github.com/jordipons/EUSIPCO2017) |
| [Monoaural audio source separation using deep convolutional neural networks](http://mtg.upf.edu/system/files/publications/monoaural-audio-source_0.pdf) | [GitHub](https://github.com/MTG/DeepConvSep) |
| [Singing voice melody transcription using deep neural networks](https://wp.nyu.edu/ismir2016/wp-content/uploads/sites/2294/2016/07/163_Paper.pdf) | No |
| [Singing voice separation using deep neural networks and F0 estimation](http://www.music-ir.org/mirex/abstracts/2016/RSGP1.pdf) | [Website](http://cvssp.org/projects/maruss/mirex2016/) |
| [Improved musical onset detection with convolutional neural networks](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202014/papers/p7029-schluter.pdf) | No |
| [Exploring data augmentation for improved singing voice detection with neural networks](https://grrrr.org/pub/schlueter-2015-ismir.pdf) | [GitHub](https://github.com/f0k/ismir2015) |
| [Learning to pinpoint singing voice from weakly labeled examples](http://www.ofai.at/~jan.schlueter/pubs/2016_ismir.pdf) | No |
| [Deep learning for event detection, sequence labelling and similarity estimation in music signals](http://ofai.at/~jan.schlueter/pubs/phd/phd.pdf) | No |
| [Musical onset detection with convolutional neural networks](http://phenicx.upf.edu/system/files/publications/Schlueter_MML13.pdf) | No |
| [Music feature maps with convolutional neural networks for music genre classification](https://www.researchgate.net/profile/Thomas_Pellegrini/publication/319326354_Music_Feature_Maps_with_Convolutional_Neural_Networks_for_Music_Genre_Classification/links/59ba5ae3458515bb9c4c6724/Music-Feature-Maps-with-Convolutional-Neural-Networks-for-Music-Genre-Classification.pdf?origin=publication_detail&ev=pub_int_prw_xdl&msrp=wzXuHZAa5zAnqEmErYyZwIRr2H0q01LnNEd4Wd7A15CQfdVLwdy98pmE-AdnrDvoc3-bVENSFrHt0yhaOiE2mQrYllVS9CJZOk-c9R0j_R1rbgcZugS6RtQ_.AUjPuJSF5P_DMngf-woH7W-7jdnQlbNQziR4_h6NnCHfR_zGcEa8vOyyOz5gx5nc4azqKTPQ5ZgGGLUxkLj1qCQLEQ5ThkhGlWHLyA.s6MBZE20-EO_RjRGCOCV4wk0WSFdN56Aloiraxz9hKCbJwRM2Et27RHVUA8jj9H8qvXIB6f7zSIrQgjXGrL2yCpyQlLffuf57rzSwg.KMMXbZrHsihV8DJM53xkHAWf3VebCJESi4KU4btNv9nQsyK2KnkhSQaTILKv0DSZY3c70a61LzywCBuoHtIhVOFhW5hVZN2n5O9uKQ) | No |
| [Singer traits identification using deep neural network](https://cs224d.stanford.edu/reports/SkiZhengshan.pdf) | No |
| [A hybrid recurrent neural network for music transcription](https://arxiv.org/pdf/1411.1623.pdf) | No |
| [An end-to-end neural network for polyphonic music transcription](https://arxiv.org/pdf/1508.01774.pdf) | No |
| [Deep karaoke: Extracting vocals from musical mixtures using a convolutional deep neural network](https://link.springer.com/chapter/10.1007/978-3-319-22482-4_50) | No |
| [Automatic drum transcription for polyphonic recordings using soft attention mechanisms and convolutional neural networks](http://www.ryanstables.co.uk/docs/ISMIR2017CamReady.pdf) | [GitHub](https://github.com/CarlSouthall/ADTLib) |
| [Analysis of time-frequency representations for musical onset detection with convolutional neural network](http://ieeexplore.ieee.org/abstract/document/7733228/) | No |
| [Note onset detection in musical signals via neural-network-based multi-ODF fusion](https://www.degruyter.com/downloadpdf/j/amcs.2016.26.issue-1/amcs-2016-0014/amcs-2016-0014.pdf) | No |
| [Folk music style modelling by recurrent neural networks with long short term memory units](http://ismir2015.uma.es/LBD/LBD13.pdf) | [GitHub](https://github.com/IraKorshunova/folk-rnn) |
| [Music transcription modelling and composition using deep learning](https://drive.google.com/file/d/0B1OooSxEtl0FcTBiOGdvSTBmWnc/view) | [GitHub](https://github.com/IraKorshunova/folk-rnn) |
| [Taking the models back to music practice: Evaluating generative transcription models built using deep learning](http://jcms.org.uk/issues/Vol2Issue1/taking-models-back-to-music-practice/Taking%20the%20Models%20back%20to%20Music%20Practice:%20Evaluating%20Generative%20Transcription%20Models%20built%20using%20Deep%20Learning.pdf) | [GitHub](https://github.com/IraKorshunova/folk-rnn) |
| [Convolutional neural network for robust pitch determination](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202016/pdfs/0000579.pdf) | No |
| [Deep convolutional neural networks and data augmentation for acoustic event detection](https://arxiv.org/pdf/1604.07160.pdf) | No |
| [Generating nontrivial melodies for music as a service](https://ismir2017.smcnus.org/wp-content/uploads/2017/10/178_Paper.pdf) | No |
| A sequential network design for musical applications | No |
| [A connectionist approach to algorithmic composition](http://www.jstor.org/stable/3679551) | No |
| [Deep neural network based instrument extraction from music](https://www.researchgate.net/profile/Stefan_Uhlich/publication/282001406_Deep_neural_network_based_instrument_extraction_from_music/links/5600eeda08ae07629e52b397/Deep-neural-network-based-instrument-extraction-from-music.pdf) | No |
| [Boundary detection in music structure analysis using convolutional neural networks](https://dav.grrrr.org/public/pub/ullrich_schlueter_grill-2014-ismir.pdf) | No |
| [A hybrid DSP/deep learning approach to real-time full-band speech enhancement](https://arxiv.org/pdf/1709.08243.pdf) | [GitHub](https://github.com/xiph/rnnoise/) |
| [Deep content-based music recommendation](http://papers.nips.cc/paper/5004-deep-content-based-music-recommendation.pdf) | No |
| [Convolutional methods for music analysis](http://vbn.aau.dk/files/260308151/PHD_Gissel_Velarde_E_pdf.pdf) | No |
| [Extending temporal feature integration for semantic audio analysis](http://www.aes.org/e-lib/browse.cfm?elib=18682) | No |
| [Recognition and retrieval of sound events using sparse coding convolutional neural network](http://ieeexplore.ieee.org/abstract/document/8019552/) | No |
| [A two-stage approach to note-level transcription of a specific piano](http://www.mdpi.com/2076-3417/7/9/901/htm) | No |
| [Improving content-based and hybrid music recommendation using deep learning](http://www.smcnus.org/wp-content/uploads/2014/08/reco_MM14.pdf) | No |
| [Audio spectrogram representations for processing with convolutional neural networks](http://dorienherremans.com/dlm2017/papers/wyse2017spect.pdf) | [Website](http://lonce.org/research/audioST/) |
| [Unsupervised learning of local features for music classification](http://www.ismir2012.ismir.net/event/papers/139_ISMIR_2012.pdf) | No |
| [Unsupervised feature learning based on deep models for environmental audio tagging](https://arxiv.org/pdf/1607.03681.pdf) | No |
| [Surrey-CVSSP system for DCASE2017 challenge task4](https://www.cs.tut.fi/sgn/arg/dcase2017/documents/challenge_technical_reports/DCASE2017_Xu_146.pdf) | [GitHub](https://github.com/yongxuUSTC/dcase2017_task4_cvssp) |
| [A study on LSTM networks for polyphonic music sequence modelling](https://qmro.qmul.ac.uk/xmlui/handle/123456789/24946) | [Website](http://www.eecs.qmul.ac.uk/~ay304/code/ismir17) |
| [Attention and localization based on a deep convolutional recurrent model for weakly supervised audio tagging](https://arxiv.org/pdf/1703.06052.pdf) | [GitHub](https://github.com/yongxuUSTC/att_loc_cgrnn) |
| [A deep representation for invariance and music classification](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202014/papers/p7034-zhang.pdf) | No |
| [A deep neural network for modeling music](https://www.researchgate.net/profile/Xiaoqing_Zheng3/publication/275347034_A_Deep_Neural_Network_for_Modeling_Music/links/5539d2060cf2239f4e7dad0d/A-Deep-Neural-Network-for-Modeling-Music.pdf) | No |

## DL4M details

All details for each article are stored in the corresponding bib entry in [dl4m.bib](dl4m.bib). Each entry has the regular bib field:

- `author`
- `year`
- `title`
- `journal` or `booktitle`

Each entry in [dl4m.bib](dl4m.bib) also displays additional information:

- `link` - HTML link to the PDF file
- `code` - Link to the source code if available
- `archi` - Neural network architecture
- `layer` - Number of layers
- `task` - The proposed tasks studied in the article
- `dataset` - The names of the dataset used
- `dataaugmentation` - The type of data augmentation technique used
- `time` - The computation time
- `hardware` - The hardware used
- `note` - Additional notes and information
- `repro` - Indication to what extent the experiments are reproducible

## Code without articles

- [Audio Classifier in Keras using Convolutional Neural Network](https://github.com/drscotthawley/audio-classifier-keras-cnn)
- [Deep learning driven jazz generation using Keras & Theano](https://github.com/jisungk/deepjazz)
- [End-to-end learning for music audio tagging at scale](https://github.com/jordipons/music-audio-tagging-at-scale-models)
- [Music Genre classification on GTZAN dataset using CNNs](https://github.com/Hguimaraes/gtzan.keras)
- [Pitch Estimation of Choir Music using Deep Learning Strategies: from Solo to Unison Recordings](https://github.com/helenacuesta/choir-pitch-estimation)

## Statistics and visualisations

- 142 papers referenced. See the details in [dl4m.bib](dl4m.bib).
- 290 unique researchers. See the list of [authors](authors.md).
- 26 tasks investigated. See the list of [tasks](tasks.md).
- 26 datasets used. See the list of [datasets](datasets.md).
- Number of articles per year:
![Number of articles per year](fig/articles_per_year.png)

## How To Contribute

Contributions are welcome!
Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## FAQ

> How are the articles sorted?

The articles are first sorted by decreasing year (to keep up with the latest news) and then alphabetically by the main author's family name.

> Why are preprint from arXiv included in the list?

I want to have exhaustive research and the latest news on DL4M. However, one should take care of the information provided in the articles currently in review. If possible you should wait for the final accepted and peer-reviewed version before citing an arXiv paper. I regularly update the arXiv links to the corresponding published papers when available.

> How much can I trust the results published in an article?

The list provided here does not guarantee the quality of the articles. You should either try to reproduce the experiments described or submit a request to [ReScience](https://github.com/ReScience/ReScience). Use one article's conclusion at your own risks.

## Acronyms used

A list of useful acronyms used in deep learning and music is stored in [acronyms.md](acronyms.md).

## Sources

The list of conferences, journals and aggregators used to gather the proposed materials is stored in [sources.md](sources.md). 

## Contributors

- [Yann Bayle](http://yannbayle.fr/english/index.php) ([GitHub](https://github.com/ybayle)) - Instigator and principal maintainer 
- Vincent Lostanlen ([GitHub](https://github.com/lostanlen))
- [Keunwoo Choi](https://keunwoochoi.wordpress.com/) ([GitHub](https://github.com/keunwoochoi))
- [Bob L. Sturm](http://www.eecs.qmul.ac.uk/~sturm/) ([GitHub](https://github.com/boblsturm))
- [Stefan Balke](https://www.audiolabs-erlangen.de/fau/assistant/balke) ([GitHub](https://github.com/stefan-balke))
- [Jordi Pons](http://www.jordipons.me/) ([GitHub](https://github.com/jordipons))

## Other useful related lists and resources

#### Audio

- [Slides on DL4M](http://www.jordipons.me/media/DL4Music_Pons.pdf) - A personal (re)view of the state-of-the-art by [Jordi Pons](http://www.jordipons.me/)
- [DL4MIR tutorial](https://github.com/marl/dl4mir-tutorial) - Python tutorials for learning to solve MIR tasks with DL
- [Awesome Python Scientific Audio](https://github.com/faroit/awesome-python-scientific-audio) - Python resources for Audio and Machine Learning
- [ISMIR resources](http://ismir.net/resources.php) - Community maintained list
- [ISMIR Google group](https://groups.google.com/a/ismir.net/forum/#!forum/community) - Daily dose of general MIR
- [Awesome Python](https://github.com/vinta/awesome-python#audio) - Audio section of Python resources
- [Awesome Web Audio](https://github.com/notthetup/awesome-webaudio) - WebAudio packages and resources
- [Awesome Music](https://github.com/ciconia/awesome-music) - Music softwares
- [Awesome Music Production](https://github.com/adius/awesome-music-production) - Music creation
- [The Asimov Institute](http://www.asimovinstitute.org/analyzing-deep-learning-tools-music/) - 6 deep learning tools for music generation
- [DLM Google group](https://groups.google.com/forum/#!forum/icdlm) - Deep Learning in Music group
- [MIR community on Slack](https://slackpass.io/mircommunity) - Link to subscribe to the MIR community's Slack

#### Music datasets

- [AudioContentAnalysis nearly exhaustive list of music-related datasets](http://www.audiocontentanalysis.org/data-sets/)
- [Teaching MIR](https://teachingmir.wikispaces.com/Datasets)
- [Wikipedia's list of datasets for machine learning research](https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research#cite_ref-215)
- [Datasets for deep learning](http://deeplearning.net/datasets/)
- [Awesile public datasets](https://github.com/caesar0301/awesome-public-datasets)

#### Deep learning

- [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning) - General deep learning resources
- [Awesome Deep Learning Resources](https://github.com/endymecy/awesome-deeplearning-resources) - Papers regarding deep learning and deep reinforcement learning
- [Awesome RNNs](https://github.com/kjw0612/awesome-rnn) - RNNs code, theory and applications
- [Cheatsheets AI](https://github.com/kailashahirwar/cheatsheets-ai) - Cheat Sheets for Keras, neural networks, scikit-learn,...
- [DL PaperNotes](https://github.com/dennybritz/deeplearning-papernotes) - Summaries and notes on general deep learning research papers 
- General [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) lists
