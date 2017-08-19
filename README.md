# Deep Learning for Music (DL4M) ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

The role of this curated list is to gather scientific articles that use deep learning approaches applied to music.
The list is currently under construction but feel free to contribute to the missing fields and to add other resources.

## Table of contents

- [DL4M summary](#dl4m-summary)
- [DL4M details](#dl4m-details)
- [Code without articles](#code-without-articles)
- [Statistics and visualisations](#statistics-and-visualisations)
- [How To Contribute](#how-to-contribute)
- [FAQ](#faq)
- [Abbreviations used](#abbreviations-used)
- [Sources](#sources)
- [Contributors](#contributors)
- [Other useful related lists](#other-useful-related-lists)

## DL4M summary 

| Article | Code |
|---------------------|-------------------------|
| [Transfer learning for music classification and regression tasks](https://arxiv.org/pdf/1703.09179v3.pdf) | [GitHub](https://arxiv.org/pdf/1703.09179v3.pdf) |
| [Convolutional recurrent neural networks for music classification](http://ieeexplore.ieee.org/abstract/document/7952585/) | [GitHub](http://ieeexplore.ieee.org/abstract/document/7952585/) |
| [An evaluation of convolutional neural networks for music classification using spectrograms](http://www.inf.ufpr.br/lesoliveira/download/ASOC2017.pdf) | No |
| [Music signal processing using vector product neural networks](https://arxiv.org/pdf/1706.09555.pdf) | No |
| [Transforming musical signals through a genre classifying convolutional neural network](https://arxiv.org/pdf/1706.09553.pdf) | No |
| [Deep convolutional neural networks for predominant instrument recognition in polyphonic music](http://dl.acm.org/citation.cfm?id=3068697) | No |
| [CNN architectures for large-scale audio classification](https://arxiv.org/pdf/1609.09430v2.pdf) | No |
| [End-to-end musical key estimation using a convolutional neural network](https://arxiv.org/pdf/1706.02921.pdf) | |
| [Sample-level deep convolutional neural networks for music auto-tagging using raw waveforms](https://arxiv.org/pdf/1703.01789v2.pdf) | |
| [Multi-level and multi-scale feature aggregation using sample-level deep convolutional neural networks for music classification](https://arxiv.org/pdf/1706.06810.pdf) | |
| [Melody extraction and detection through LSTM-RNN with harmonic sum loss](http://ieeexplore.ieee.org/abstract/document/7952660/) | |
| [Timbre analysis of music audio signals with convolutional neural networks](https://arxiv.org/pdf/1703.06697.pdf) | [GitHub](https://arxiv.org/pdf/1703.06697.pdf) |
| [Designing efficient architectures for modeling temporal features with convolutional neural networks](http://ieeexplore.ieee.org/document/7952601/) | [GitHub](http://ieeexplore.ieee.org/document/7952601/) |
| [Music feature maps with convolutional neural networks for music genre classification](https://www.micc.unifi.it/cbmi2017/session/poster-and-demo-session/) | No |
| [Extending temporal feature integration for semantic audio analysis](http://www.aes.org/e-lib/browse.cfm?elib=18682) | No |
| [Audio spectrogram representations for processing with convolutional neural networks](https://arxiv.org/pdf/1706.09559.pdf) | No |
| [A study on lstm networks for polyphonic music sequence modelling](https://qmro.qmul.ac.uk/xmlui/handle/123456789/24946) | [Website](https://qmro.qmul.ac.uk/xmlui/handle/123456789/24946) |
| [An efficient approach for segmentation, feature extraction and classification of audio signals ](http://file.scirp.org/pdf/CS_2016042615054817.pdf) | No |
| [Towards playlist generation algorithms using rnns trained on within-track transitions](https://arxiv.org/pdf/1606.02096.pdf) | No |
| [Automatic tagging using deep convolutional neural networks](https://arxiv.org/pdf/1606.00298.pdf) | No |
| [Automatic chord estimation on seventhsbass chord vocabulary using deep neural network](http://ieeexplore.ieee.org/abstract/document/7471677/) | |
| [Robust downbeat tracking using an ensemble of convolutional networks](http://ieeexplore.ieee.org/abstract/document/7728057/) | |
| [Bayesian meter tracking on learned signal representations](http://www.rhythmos.org/MMILab-Andre_files/ISMIR2016_CNNDBNbeats_camready.pdf) | |
| [Learning temporal features using a deep neural network and its application to music genre classification](https://www.researchgate.net/profile/Il_Young_Jeong/publication/305683876_Learning_temporal_features_using_a_deep_neural_network_and_its_application_to_music_genre_classification/links/5799a27c08aec89db7bb9f92.pdf) | |
| [On the potential of simple framewise approaches to piano transcription](https://arxiv.org/abs/1612.05153) | |
| [Feature learning for chord recognition: the deep chroma extractor](https://arxiv.org/pdf/1612.05065.pdf) | |
| [A deep bidirectional long short-term memory based multi-scale approach for music dynamic emotion prediction](http://ieeexplore.ieee.org/document/7471734/) | |
| [Event localization in music auto-tagging](http://mac.citi.sinica.edu.tw/~yang/pub/liu16mm.pdf) | [GitHub](http://mac.citi.sinica.edu.tw/~yang/pub/liu16mm.pdf) |
| [Deep convolutional networks on the pitch spiral for musical instrument recognition](https://github.com/lostanlen/ismir2016/blob/master/paper/lostanlen_ismir2016.pdf) | |
| [Robust audio event recognition with 1-max pooling convolutional neural networks](https://arxiv.org/pdf/1604.06338.pdf) | No |
| [Singing voice melody transcription using deep neural networks](https://wp.nyu.edu/ismir2016/wp-content/uploads/sites/2294/2016/07/163_Paper.pdf) | |
| [Singing voice separation using deep neural networks and F0 estimation](http://www.music-ir.org/mirex/abstracts/2016/RSGP1.pdf) | [Website](http://www.music-ir.org/mirex/abstracts/2016/RSGP1.pdf) |
| [Learning to pinpoint singing voice from weakly labeled examples](http://www.ofai.at/~jan.schlueter/pubs/2016_ismir.pdf) | |
| [Note onset detection in musical signals via neuralÃ¢â‚¬â€œnetworkÃ¢â‚¬â€œbased multiÃ¢â‚¬â€œodf fusion](https://www.degruyter.com/downloadpdf/j/amcs.2016.26.issue-1/amcs-2016-0014/amcs-2016-0014.pdf) | No |
| [Convolutional neural network for robust pitch determination](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202016/pdfs/0000579.pdf) | |
| [Deep convolutional neural networks and data augmentation for acoustic event detection](https://arxiv.org/pdf/1604.07160.pdf) | No |
| [Unsupervised feature learning based on deep models for environmental audio tagging](https://arxiv.org/pdf/1607.03681.pdf) | |
| [Auralisation of deep convolutional neural networks: listening to learned features](http://ismir2015.uma.es/LBD/LBD24.pdf) | |
| [Downbeat tracking with multiple features and deep neural networks](http://perso.telecom-paristech.fr/~grichard/Publications/2015-durand-icassp.pdf) | |
| [Music boundary detection using neural networks on spectrograms and self-similarity lag matrices](http://www.ofai.at/~jan.schlueter/pubs/2015_eusipco.pdf) | |
| [Classification of spatial audio location and content using convolutional neural networks](https://www.researchgate.net/profile/Toni_Hirvonen/publication/276061831_Classification_of_Spatial_Audio_Location_and_Content_Using_Convolutional_Neural_Networks/links/5550665908ae12808b37fe5a/Classification-of-Spatial-Audio-Location-and-Content-Using-Convolutional-Neural-Networks.pdf) | |
| [Deep learning, audio adversaries, and music content analysis](http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6905/pdf/imm6905.pdf) | |
| [Singing voice detection with deep recurrent neural networks](https://hal-imt.archives-ouvertes.fr/hal-01110035/document) | |
| [Automatic instrument recognition in polyphonic music using convolutional neural networks](https://arxiv.org/pdf/1511.05520.pdf) | |
| [A software framework for musical data augmentation](https://bmcfee.github.io/papers/ismir2015_augmentation.pdf) | |
| [A deep bag-of-features model for music auto-tagging](https://arxiv.org/pdf/1508.04999v1.pdf) | |
| [Music-noise segmentation in spectrotemporal domain using convolutional neural networks](http://ismir2015.uma.es/LBD/LBD27.pdf) | |
| [Musical instrument sound classification with deep convolutional neural network using feature fusion approach](https://arxiv.org/ftp/arxiv/papers/1512/1512.07370.pdf) | |
| [Environmental sound classification with convolutional neural networks](https://scholar.google.co.kr/scholar?hl=en&q=Environmental+sound+classification+with+convolutional+neural+networks&btnG=&as_sdt=1%2C5&as_sdtp=) | |
| [Exploring data augmentation for improved singing voice detection with neural networks](https://grrrr.org/pub/schlueter-2015-ismir.pdf) | No |
| [An end-to-end neural network for polyphonic music transcription](https://arxiv.org/pdf/1508.01774.pdf) | |
| [Deep karaoke: extracting vocals from musical mixtures using a convolutional deep neural network](https://link.springer.com/chapter/10.1007/978-3-319-22482-4_50) | |
| [Deep neural network based instrument extraction from music](https://www.researchgate.net/profile/Stefan_Uhlich/publication/282001406_Deep_neural_network_based_instrument_extraction_from_music/links/5600eeda08ae07629e52b397/Deep-neural-network-based-instrument-extraction-from-music.pdf) | |
| [A deep neural network for modeling music](https://www.researchgate.net/profile/Xiaoqing_Zheng3/publication/275347034_A_Deep_Neural_Network_for_Modeling_Music/links/5539d2060cf2239f4e7dad0d/A-Deep-Neural-Network-for-Modeling-Music.pdf) | |
| [The munich lstm-rnn approach to the mediaeval 2014 Ã¢â‚¬Å“emotion in musicÃ¢â‚¬Â task](https://pdfs.semanticscholar.org/8a24/c5131d5a28165f719697028c34b00e6d3f60.pdf) | |
| [End-to-end learning for music audio](http://ieeexplore.ieee.org/abstract/document/6854950/) | No |
| [Deep learning for music genre classification](https://courses.engr.illinois.edu/ece544na/fa2014/Tao_Feng.pdf) | No |
| [Recognition of acoustic events using deep neural networks](https://www.cs.tut.fi/sgn/arg/music/tuomasv/dnn_eusipco2014.pdf) | |
| [Deep image features in music information retrieval](https://www.degruyter.com/downloadpdf/j/eletel.2014.60.issue-4/eletel-2014-0042/eletel-2014-0042.pdf) | |
| [From music audio to chord tablature: teaching deep convolutional networks to play guitar](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202014/papers/p7024-humphrey.pdf) | |
| [Improved musical onset detection with convolutional neural networks](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202014/papers/p7029-schluter.pdf) | No |
| [A hybrid recurrent neural network for music transcription](https://arxiv.org/pdf/1411.1623.pdf) | |
| [Boundary detection in music structure analysis using convolutional neural networks](https://dav.grrrr.org/public/pub/ullrich_schlueter_grill-2014-ismir.pdf) | |
| [Improving content-based and hybrid music recommendation using deep learning](http://www.smcnus.org/wp-content/uploads/2014/08/reco_MM14.pdf) | |
| [A deep representation for invariance and music classification](https://arxiv.org/pdf/1404.0400.pdf) | |
| [Multiscale approaches to music audio feature learning](http://ismir2013.ismir.net/wp-content/uploads/2013/09/69_Paper.pdf) | |
| [Deep content-based music recommendation](http://papers.nips.cc/paper/5004-deep-content-based-music-recommendation.pdf) | |
| [Musical onset detection with convolutional neural networks](http://phenicx.upf.edu/system/files/publications/Schlueter_MML13.pdf) | |
| [Rethinking automatic chord recognition with convolutional neural networks](http://ieeexplore.ieee.org/document/6406762/) | |
| [Moving beyond feature design: deep architectures and automatic feature learning in music informatics](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.294.2304&rep=rep1&type=pdf) | |
| [Local-feature-map integration using convolutional neural networks for music genre classification.](http://liris.cnrs.fr/Documents/Liris-5602.pdf) | |
| [Learning sparse feature representations for music annotation and retrieval](https://pdfs.semanticscholar.org/099d/85f25e9336f48ff64287a4b53ee5fb64ab51.pdf) | No |
| [Unsupervised learning of local features for music classification.](http://www.ismir2012.ismir.net/event/papers/139_ISMIR_2012.pdf) | |
| [Audio-based music classification with a pretrained convolutional network](http://www.ismir2011.ismir.net/papers/PS6-3.pdf) | |
| [Automatic musical pattern feature extraction using convolutional neural network](https://www.researchgate.net/profile/Antoni_Chan2/publication/44260643_Automatic_Musical_Pattern_Feature_Extraction_Using_Convolutional_Neural_Network/links/02e7e523dac6bb86b0000000.pdf) | |
| [Audio musical genre classification using convolutional neural networks and pitch and tempo transformations](http://lbms03.cityu.edu.hk/theses/c_ftt/mphil-cs-b39478026f.pdf) | |
| [Unsupervised feature learning for audio classification using convolutional deep belief networks](http://papers.nips.cc/paper/3674-unsupervised-feature-learning-for-audio-classification-using-convolutional-deep-belief-networks.pdf) | No |
| [A convolutional-kernel based approach for note onset detection in piano-solo audio signals](http://www.murase.nuie.nagoya-u.ac.jp/~ide/res/paper/E04-conference-pablo-1.pdf) | |
| [A supervised learning approach to musical style recognition](https://www.researchgate.net/profile/Giuseppe_Buzzanca/publication/228588086_A_supervised_learning_approach_to_musical_style_recognition/links/54b43ee90cf26833efd0109f.pdf) | |

## DL4M details

- [dl4m.bib](dl4m.bib) - the corresponding bibliography.
- [dl4m.tsv](dl4m.tsv) - more details about each article:
	- First author name
	- Publication year
	- Article name
	- PDF link
	- Source code link
	- Source code reproducible (Yes/No) If Yes, indicates to what extent
	- Neural network architecture
	- Number of layers
	- Task
	- Dataset
	- Computation time
	- Hardware
	- Data augmentation technique if used
	- Additional notes

## Code without articles

- [Audio Classifier in Keras using Convolutional Neural Network](https://github.com/drscotthawley/audio-classifier-keras-cnn)

## Statistics and visualisations

- 79 articles currently referenced.
- Number of articles per year:
![Number of articles per year](fig/articles_per_year.png)

## How To Contribute

1. Adding/Updating information
	1. Fork the repo.
	2. Add one line per article in [dl4m.tsv](dl4m.tsv) with every column correctly filled.
	3. Submit your pull request and that's it! (Note: the table in the ReadMe is automatically generated thanks to a python script.)
2. Visualisation
	- Please submit your idea for new visualisation of the data
	- I am looking for a way to display relations between articles automatically like a mindmap. Tell me if you know anything able to handle that.

## FAQ

> Why a tsv file instead of a regular csv file for storing the detailed information about the articles?

Because:
1. Some articles have a comma in their title and the .bib of each article contains commas.
2. [GitHub currently only displays csv and tsv files](https://help.github.com/articles/rendering-csv-and-tsv-data/).
The built-in GitHub csv/tsv parser is handy because you can easily search in the file in your browser without downloading anything.

> How are the articles sorted?

In [dl4m.tsv](dl4m.tsv), the articles are sorted by decreasing year (to keep up with the latest news) and then alphabetically.

## Abbreviations used

| Abbreviation | Full name |
|--------------|-----------|
| DNN | Deep Neural Network |
| CNN | Convolutional Neural Network |
| RNN | Recurrent Neural Network |
| VPNN | Vector Product Neural Network |
| VAD | Voice Activity Detection |
| SVS | Singing Voice Separation |
| SVD | Singing Voice Detection |

## Sources

#### Conferences and journals

- [ISMIR](http://ismir.net/)
- [MIREX](http://ismir.net/)
- [ICASSP](http://ismir.net/)
- [SMC](http://ismir.net/)
- [IWDLM](http://ismir.net/)

#### Aggregators 

- [PaperScape](http://paperscape.org/)
- [arXiv](https://arxiv.org/)
- [SciRate](https://scirate.com/)
- [Scholar](https://scholar.google.com/scholar?q=neural+network+audio+music)

## Contributors

- [Vincent Lostanlen](https://github.com/lostanlen)
- [Keunwoo Choi](https://github.com/keunwoochoi)

## Other useful related lists

- [Awesome Python Scientific Audio](https://github.com/faroit/awesome-python-scientific-audio) - Python resources for Audio and Machine Learning
- [Cheatsheets AI](https://github.com/kailashahirwar/cheatsheets-ai) - Cheat Sheets for Keras, neural networks, scikit-learn,...
- [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning) - General deep learning resources
- [ISMIR resources](http://ismir.net/resources.php) - Community maintained list
- [Awesome Python](https://github.com/vinta/awesome-python#audio) - Audio section of Python resources
- [Awesome Web Audio](https://github.com/notthetup/awesome-webaudio) - WebAudio packages and resources
- [Awesome Music](https://github.com/ciconia/awesome-music) - Music softwares
- [Awesome Music Production](https://github.com/adius/awesome-music-production) - Music creation
- General [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) lists
