Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

=========== RESTART: D:/Sem4/KBDVM/MOULI/ML/BL.SC.U4AIE24143_LAB02.py ==========

Purchase Data
Features: 3
Records: 10
Rank: 3
Cost of Candies: 0.9999999999999989
Cost of Mangoes: 54.99999999999999
Cost of Milk Packets: 18.0

Customer Classification
   Payment (Rs) Status
0           386   RICH
1           289   RICH
2           393   RICH
3           110   POOR
4           280   RICH
5           167   POOR
6           271   RICH
7           274   RICH
8           148   POOR
9           198   POOR

Stock Analysis
Manual Mean: 1560.6634538152598
Manual Variance: 58496.49239931618
Execution Time: 7.152557373046875e-05
Loss Probability: 0.4979919678714859
Wednesday Mean: 1550.7060000000004
April Mean: 1698.9526315789474
Conditional Profit: 0.42

Thyroid Dataset
Datatypes:
 Record ID                     int64
age                           int64
sex                          object
on thyroxine                 object
query on thyroxine           object
on antithyroid medication    object
sick                         object
pregnant                     object
thyroid surgery              object
I131 treatment               object
query hypothyroid            object
query hyperthyroid           object
lithium                      object
goitre                       object
tumor                        object
hypopituitary                object
psych                        object
TSH measured                 object
TSH                          object
T3 measured                  object
T3                           object
TT4 measured                 object
TT4                          object
T4U measured                 object
T4U                          object
FTI measured                 object
FTI                          object
TBG measured                 object
TBG                          object
referral source              object
Condition                    object
dtype: object

Missing Values:
 Record ID                    0
age                          0
sex                          0
on thyroxine                 0
query on thyroxine           0
on antithyroid medication    0
sick                         0
pregnant                     0
thyroid surgery              0
I131 treatment               0
query hypothyroid            0
query hyperthyroid           0
lithium                      0
goitre                       0
tumor                        0
hypopituitary                0
psych                        0
TSH measured                 0
TSH                          0
T3 measured                  0
T3                           0
TT4 measured                 0
TT4                          0
T4U measured                 0
T4U                          0
FTI measured                 0
FTI                          0
TBG measured                 0
TBG                          0
referral source              0
Condition                    0
dtype: int64

Statistics:
           Record ID           age
count  9.172000e+03   9172.000000
mean   8.529473e+08     73.555822
std    7.581969e+06   1183.976718
min    8.408010e+08      1.000000
25%    8.504090e+08     37.000000
50%    8.510040e+08     55.000000
75%    8.607110e+08     68.000000
max    8.701190e+08  65526.000000

Similarity Measures
Jaccard Coefficient: 0
Simple Matching Coefficient: 0
Cosine Similarity: 0.9999999999999997

After Imputation
Record ID                    0
age                          0
sex                          0
on thyroxine                 0
query on thyroxine           0
on antithyroid medication    0
sick                         0
pregnant                     0
thyroid surgery              0
I131 treatment               0
query hypothyroid            0
query hyperthyroid           0
lithium                      0
goitre                       0
tumor                        0
hypopituitary                0
psych                        0
TSH measured                 0
TSH                          0
T3 measured                  0
T3                           0
TT4 measured                 0
TT4                          0
T4U measured                 0
T4U                          0
FTI measured                 0
FTI                          0
TBG measured                 0
TBG                          0
referral source              0
Condition                    0
dtype: int64

Normalization
      Record ID       age sex  ... TBG referral source     Condition
0  0.000000e+00  0.000427   F  ...   ?           other  NO CONDITION
1  3.410871e-08  0.000427   F  ...   ?           other  NO CONDITION
2  9.891527e-07  0.000610   F  ...  11           other  NO CONDITION
3  6.934301e-05  0.000534   F  ...  26           other  NO CONDITION
4  6.937712e-05  0.000473   F  ...  36           other             S

[5 rows x 31 columns]
