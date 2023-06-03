import timeit


# Copied from to_01list.py
def to_01list(n):
    """
    convert n into binary representation
    list of bits starts with lsb.
    """
    if n == 0:
        '''
        strange case, because zero is not the empty word, but 0
        '''
        return [0]
    else:
        res = []
        while n > 0:
            res.append(n % 2)
            n = n // 2
        return res


# Task 1:
def bin_inc(list_to_increment: list):
    """
    Non-mutative bitwise incrementation of a binary number represented as a list.
    Runtime analysis:
    n is proportional to the length of list_to_increment:
    Has O(n) runtime in the average case and maximal case.
    Has O(1) runtime in the minimal case that the list_to_increment is empty or has only one element.
    :param list_to_increment: the list to increment :return: list_to_increment + 1
    """
    # Constant runtime
    new_list = [0] * len(list_to_increment)
    # Constant runtime
    carry = 1

    # Repeat len(list_to_increment) times. In case of carry == 0 after addition,
    # there will be constantly fewer operations (since we don't have to add anymore),
    # which doesn't matter for the runtime analysis.
    for i in range(len(list_to_increment)):
        # Constant runtime
        new_list[i] = (list_to_increment[i] ^ carry)  # 0 ^ 0 -> 0, 1 ^ 0 -> 1, 1 ^ 1 -> 0, 0 ^ 0 -> 0
        # Constant runtime
        carry = list_to_increment[i] & carry
        # If there is no carry left over (there was an addition with exact result 0 or 1) then fill the rest and return.
        # Comparison has constant runtime
        if carry == 0:
            # Has O(n) whereas n = len(list_to_increment) - i.
            new_list[i + 1:] = list_to_increment[i + 1:]
            # Constant runtime
            return new_list
    # Constant runtime
    if carry == 1:
        # Constant runtime
        new_list.append(1)
    # Constant runtime
    return new_list


# Tests:
# print(bin_inc([0, 1, 1]))  # -> [1, 1, 1]
# print(bin_inc([1, 0, 1]))  # -> [0, 1, 1]

# Print binary numbers from 0 + 1 to 15 + 1
# for i in range(0, 16):
# print(bin_inc(to_01list(i)))


# Task 2:
def bin_inc_mut(n):
    """
    Mutative incrementation of a binary number in list format.
    Runtime analysis:
    n is proportional to the length of list_to_increment:
    Has O(n) runtime in the average and maximal case.
    The average case is still a lot faster than the maximal case because the program stops after realising that
    there is no point to continue adding since the carry is 0.
    This is a lot faster than the average case of the non-mutative implementation,
    because the rest of the list doesn't have to be copied.
    The minimal case is the runtime of O(1) when the first bit is 0,
    which is a much more common average case than the first implementation.
    Also, it doesn't get very much worse if it isn't because the bit after that could be 0.
    :param n: List to increment
    :return: n + 1
    """
    # Constant runtime
    i = 0
    # Maximally len(n) times. Stop when the "next" bit is 0.
    # The bit after that won't have to be incremented, since 1 + 0 = 0 + 1 = 1, with carry 0
    while i < len(n) and n[i] == 1:
        # Everything at this point has a constant runtime.
        n[i] = 0
        i = i + 1
    if i == len(n):
        n.append(1)
    else:
        n[i] = 1


# Task 3:
def benchmark(n):
    i = to_01list(0)

    def benchmark1():
        global d
        d = i
        # Iterate to bin(n) with non-mutative method.
        while d != to_01list(n):
            d = bin_inc(d)

    def benchmark2():
        global d
        d = i
        # Iterate to bin(n) with mutative method.
        while d != to_01list(n):
            bin_inc_mut(d)

    # Do the stopwatching
    start = timeit.default_timer()
    benchmark1()
    end = timeit.default_timer()
    diff1 = end - start
    start = timeit.default_timer()
    benchmark2()
    end = timeit.default_timer()
    diff2 = end - start

    # Print the timings
    print(str(n) + "\t" + str(diff1) + "\t" + str(diff2))


# Run the benchmark up to 100000.
# That means this will iterate from 0 to all numbers between 0 and 100000 with both methods.
"""
for i in range(0, 100000, 1000):
    benchmark(i)
"""

# Used output for plot:
"""
0	6.999999999993123e-07	3.999999999976245e-07
1000	0.0015773000000000037	0.0011386999999999994
2000	0.0034205	0.0022362999999999966
3000	0.00503350000000001	0.0036024000000000056
4000	0.006928099999999993	0.004848999999999992
5000	0.009005199999999991	0.0063719
6000	0.010409699999999994	0.007525900000000002
7000	0.0129803	0.009180999999999995
8000	0.014506199999999997	0.01028599999999999
9000	0.016038799999999992	0.012307700000000005
10000	0.017944299999999996	0.013973399999999997
11000	0.019700300000000004	0.018823499999999993
12000	0.021923199999999976	0.015905699999999967
13000	0.02389410000000003	0.017632900000000007
14000	0.025236099999999984	0.018141000000000018
15000	0.027026099999999997	0.01981369999999999
16000	0.02968540000000003	0.02132419999999996
17000	0.031742599999999954	0.023126700000000056
18000	0.03296730000000003	0.024629000000000012
19000	0.03487000000000007	0.024922699999999964
20000	0.03705880000000006	0.026678300000000044
21000	0.03873350000000009	0.027639200000000086
22000	0.040630900000000025	0.02973579999999998
23000	0.041903899999999994	0.030944700000000047
24000	0.044415399999999994	0.03238989999999997
25000	0.04707499999999998	0.03501160000000003
26000	0.04796020000000012	0.03580990000000006
27000	0.049337399999999976	0.03663510000000003
28000	0.05250599999999994	0.038054299999999985
29000	0.0531914	0.04006810000000005
30000	0.055165300000000084	0.041347400000000034
31000	0.05653590000000008	0.042445499999999914
32000	0.06003179999999997	0.044712400000000097
33000	0.06238239999999995	0.04520919999999995
34000	0.06466029999999989	0.045990100000000034
35000	0.0693214000000002	0.04994249999999978
36000	0.06837099999999996	0.0511522000000002
37000	0.07075429999999994	0.05100339999999992
38000	0.07321489999999997	0.053546299999999825
39000	0.07410739999999993	0.05330009999999996
40000	0.0802299999999998	0.05854299999999979
41000	0.07768850000000027	0.056514799999999976
42000	0.08034160000000012	0.060457199999999656
43000	0.08387490000000009	0.060494600000000176
44000	0.08414840000000012	0.061846099999999904
45000	0.08569309999999986	0.06256830000000013
46000	0.08758210000000011	0.06342099999999995
47000	0.09453829999999996	0.06607619999999992
48000	0.09156750000000002	0.06814870000000006
49000	0.09363080000000013	0.07108209999999993
50000	0.09554379999999973	0.06980050000000038
51000	0.0970065	0.07076960000000021
52000	0.09928269999999983	0.07354539999999954
53000	0.10271739999999951	0.07476090000000024
54000	0.10347370000000033	0.07525449999999978
55000	0.10536619999999974	0.07763109999999962
56000	0.10684629999999995	0.0801734999999999
57000	0.10986829999999959	0.08496889999999979
58000	0.11027370000000047	0.08429799999999954
59000	0.11589179999999999	0.08376809999999946
60000	0.11607870000000009	0.08494299999999999
61000	0.11647370000000024	0.08619749999999993
62000	0.11862249999999985	0.09351619999999983
63000	0.12283430000000006	0.09436679999999953
64000	0.12287170000000014	0.09093420000000041
65000	0.12574669999999966	0.09404500000000038
66000	0.13129029999999986	0.09662170000000003
67000	0.13224459999999993	0.1021263999999995
68000	0.13575720000000047	0.10007300000000008
69000	0.13915640000000007	0.10223319999999969
70000	0.13873390000000008	0.10188489999999994
71000	0.1411276000000008	0.10216349999999963
72000	0.14482240000000068	0.10680169999999833
73000	0.14570210000000117	0.10866590000000009
74000	0.1477606999999992	0.11427289999999957
75000	0.14991189999999932	0.10967679999999902
76000	0.1512823000000001	0.11082719999999924
77000	0.15460649999999987	0.1192227999999993
78000	0.15613090000000085	0.11529970000000134
79000	0.15802080000000096	0.11700349999999915
80000	0.16000050000000066	0.11720940000000013
81000	0.16117100000000129	0.11990049999999997
82000	0.1648031000000003	0.1209511999999986
83000	0.16596749999999894	0.12249839999999956
84000	0.16915480000000116	0.12832990000000066
85000	0.1690170000000002	0.12454460000000012
86000	0.17098299999999966	0.1299147000000005
87000	0.173686	0.12890039999999914
88000	0.17632519999999907	0.1310640000000003
89000	0.1778267999999983	0.13347359999999853
90000	0.18421929999999875	0.1368228000000009
91000	0.18088899999999875	0.1372522000000007
92000	0.18429929999999928	0.13611090000000026
93000	0.18742969999999914	0.1379771999999999
94000	0.1901579999999985	0.14010619999999996
95000	0.18915939999999942	0.1421348000000009
96000	0.19393160000000087	0.14384400000000142
97000	0.19655820000000013	0.14380159999999975
98000	0.1998002999999997	0.14682289999999654
99000	0.1976526000000014	0.14704749999999933

Process finished with exit code 0
"""


# Task 4 Helper:
def bin_inc_mut_helper(n):
    """
    Mutative incrementation of a binary number in list format.
    Will count steps it needed to compute.
    Comparisons have been ignored for simplicity.
    """
    steps = 0
    i = 0
    steps += 1
    while i < len(n) and n[i] == 1:
        n[i] = 0
        i = i + 1
        steps += 2
    if i == len(n):
        n.append(1)
    else:
        n[i] = 1
    steps += 1
    return steps


n = to_01list(0)
i = 0
while n != to_01list(1000):
    print(str(i) + "\t" + str(bin_inc_mut_helper(n)))
    i += 1


# Gave the following output:
"""
0	2
1	4
2	2
3	6
4	2
5	4
6	2
7	8
8	2
9	4
10	2
11	6
12	2
13	4
14	2
15	10
16	2
17	4
18	2
19	6
20	2
21	4
22	2
23	8
24	2
25	4
26	2
27	6
28	2
29	4
30	2
31	12
32	2
33	4
34	2
35	6
36	2
37	4
38	2
39	8
40	2
41	4
42	2
43	6
44	2
45	4
46	2
47	10
48	2
49	4
50	2
51	6
52	2
53	4
54	2
55	8
56	2
57	4
58	2
59	6
60	2
61	4
62	2
63	14
64	2
65	4
66	2
67	6
68	2
69	4
70	2
71	8
72	2
73	4
74	2
75	6
76	2
77	4
78	2
79	10
80	2
81	4
82	2
83	6
84	2
85	4
86	2
87	8
88	2
89	4
90	2
91	6
92	2
93	4
94	2
95	12
96	2
97	4
98	2
99	6
100	2
101	4
102	2
103	8
104	2
105	4
106	2
107	6
108	2
109	4
110	2
111	10
112	2
113	4
114	2
115	6
116	2
117	4
118	2
119	8
120	2
121	4
122	2
123	6
124	2
125	4
126	2
127	16
128	2
129	4
130	2
131	6
132	2
133	4
134	2
135	8
136	2
137	4
138	2
139	6
140	2
141	4
142	2
143	10
144	2
145	4
146	2
147	6
148	2
149	4
150	2
151	8
152	2
153	4
154	2
155	6
156	2
157	4
158	2
159	12
160	2
161	4
162	2
163	6
164	2
165	4
166	2
167	8
168	2
169	4
170	2
171	6
172	2
173	4
174	2
175	10
176	2
177	4
178	2
179	6
180	2
181	4
182	2
183	8
184	2
185	4
186	2
187	6
188	2
189	4
190	2
191	14
192	2
193	4
194	2
195	6
196	2
197	4
198	2
199	8
200	2
201	4
202	2
203	6
204	2
205	4
206	2
207	10
208	2
209	4
210	2
211	6
212	2
213	4
214	2
215	8
216	2
217	4
218	2
219	6
220	2
221	4
222	2
223	12
224	2
225	4
226	2
227	6
228	2
229	4
230	2
231	8
232	2
233	4
234	2
235	6
236	2
237	4
238	2
239	10
240	2
241	4
242	2
243	6
244	2
245	4
246	2
247	8
248	2
249	4
250	2
251	6
252	2
253	4
254	2
255	18
256	2
257	4
258	2
259	6
260	2
261	4
262	2
263	8
264	2
265	4
266	2
267	6
268	2
269	4
270	2
271	10
272	2
273	4
274	2
275	6
276	2
277	4
278	2
279	8
280	2
281	4
282	2
283	6
284	2
285	4
286	2
287	12
288	2
289	4
290	2
291	6
292	2
293	4
294	2
295	8
296	2
297	4
298	2
299	6
300	2
301	4
302	2
303	10
304	2
305	4
306	2
307	6
308	2
309	4
310	2
311	8
312	2
313	4
314	2
315	6
316	2
317	4
318	2
319	14
320	2
321	4
322	2
323	6
324	2
325	4
326	2
327	8
328	2
329	4
330	2
331	6
332	2
333	4
334	2
335	10
336	2
337	4
338	2
339	6
340	2
341	4
342	2
343	8
344	2
345	4
346	2
347	6
348	2
349	4
350	2
351	12
352	2
353	4
354	2
355	6
356	2
357	4
358	2
359	8
360	2
361	4
362	2
363	6
364	2
365	4
366	2
367	10
368	2
369	4
370	2
371	6
372	2
373	4
374	2
375	8
376	2
377	4
378	2
379	6
380	2
381	4
382	2
383	16
384	2
385	4
386	2
387	6
388	2
389	4
390	2
391	8
392	2
393	4
394	2
395	6
396	2
397	4
398	2
399	10
400	2
401	4
402	2
403	6
404	2
405	4
406	2
407	8
408	2
409	4
410	2
411	6
412	2
413	4
414	2
415	12
416	2
417	4
418	2
419	6
420	2
421	4
422	2
423	8
424	2
425	4
426	2
427	6
428	2
429	4
430	2
431	10
432	2
433	4
434	2
435	6
436	2
437	4
438	2
439	8
440	2
441	4
442	2
443	6
444	2
445	4
446	2
447	14
448	2
449	4
450	2
451	6
452	2
453	4
454	2
455	8
456	2
457	4
458	2
459	6
460	2
461	4
462	2
463	10
464	2
465	4
466	2
467	6
468	2
469	4
470	2
471	8
472	2
473	4
474	2
475	6
476	2
477	4
478	2
479	12
480	2
481	4
482	2
483	6
484	2
485	4
486	2
487	8
488	2
489	4
490	2
491	6
492	2
493	4
494	2
495	10
496	2
497	4
498	2
499	6
500	2
501	4
502	2
503	8
504	2
505	4
506	2
507	6
508	2
509	4
510	2
511	20
512	2
513	4
514	2
515	6
516	2
517	4
518	2
519	8
520	2
521	4
522	2
523	6
524	2
525	4
526	2
527	10
528	2
529	4
530	2
531	6
532	2
533	4
534	2
535	8
536	2
537	4
538	2
539	6
540	2
541	4
542	2
543	12
544	2
545	4
546	2
547	6
548	2
549	4
550	2
551	8
552	2
553	4
554	2
555	6
556	2
557	4
558	2
559	10
560	2
561	4
562	2
563	6
564	2
565	4
566	2
567	8
568	2
569	4
570	2
571	6
572	2
573	4
574	2
575	14
576	2
577	4
578	2
579	6
580	2
581	4
582	2
583	8
584	2
585	4
586	2
587	6
588	2
589	4
590	2
591	10
592	2
593	4
594	2
595	6
596	2
597	4
598	2
599	8
600	2
601	4
602	2
603	6
604	2
605	4
606	2
607	12
608	2
609	4
610	2
611	6
612	2
613	4
614	2
615	8
616	2
617	4
618	2
619	6
620	2
621	4
622	2
623	10
624	2
625	4
626	2
627	6
628	2
629	4
630	2
631	8
632	2
633	4
634	2
635	6
636	2
637	4
638	2
639	16
640	2
641	4
642	2
643	6
644	2
645	4
646	2
647	8
648	2
649	4
650	2
651	6
652	2
653	4
654	2
655	10
656	2
657	4
658	2
659	6
660	2
661	4
662	2
663	8
664	2
665	4
666	2
667	6
668	2
669	4
670	2
671	12
672	2
673	4
674	2
675	6
676	2
677	4
678	2
679	8
680	2
681	4
682	2
683	6
684	2
685	4
686	2
687	10
688	2
689	4
690	2
691	6
692	2
693	4
694	2
695	8
696	2
697	4
698	2
699	6
700	2
701	4
702	2
703	14
704	2
705	4
706	2
707	6
708	2
709	4
710	2
711	8
712	2
713	4
714	2
715	6
716	2
717	4
718	2
719	10
720	2
721	4
722	2
723	6
724	2
725	4
726	2
727	8
728	2
729	4
730	2
731	6
732	2
733	4
734	2
735	12
736	2
737	4
738	2
739	6
740	2
741	4
742	2
743	8
744	2
745	4
746	2
747	6
748	2
749	4
750	2
751	10
752	2
753	4
754	2
755	6
756	2
757	4
758	2
759	8
760	2
761	4
762	2
763	6
764	2
765	4
766	2
767	18
768	2
769	4
770	2
771	6
772	2
773	4
774	2
775	8
776	2
777	4
778	2
779	6
780	2
781	4
782	2
783	10
784	2
785	4
786	2
787	6
788	2
789	4
790	2
791	8
792	2
793	4
794	2
795	6
796	2
797	4
798	2
799	12
800	2
801	4
802	2
803	6
804	2
805	4
806	2
807	8
808	2
809	4
810	2
811	6
812	2
813	4
814	2
815	10
816	2
817	4
818	2
819	6
820	2
821	4
822	2
823	8
824	2
825	4
826	2
827	6
828	2
829	4
830	2
831	14
832	2
833	4
834	2
835	6
836	2
837	4
838	2
839	8
840	2
841	4
842	2
843	6
844	2
845	4
846	2
847	10
848	2
849	4
850	2
851	6
852	2
853	4
854	2
855	8
856	2
857	4
858	2
859	6
860	2
861	4
862	2
863	12
864	2
865	4
866	2
867	6
868	2
869	4
870	2
871	8
872	2
873	4
874	2
875	6
876	2
877	4
878	2
879	10
880	2
881	4
882	2
883	6
884	2
885	4
886	2
887	8
888	2
889	4
890	2
891	6
892	2
893	4
894	2
895	16
896	2
897	4
898	2
899	6
900	2
901	4
902	2
903	8
904	2
905	4
906	2
907	6
908	2
909	4
910	2
911	10
912	2
913	4
914	2
915	6
916	2
917	4
918	2
919	8
920	2
921	4
922	2
923	6
924	2
925	4
926	2
927	12
928	2
929	4
930	2
931	6
932	2
933	4
934	2
935	8
936	2
937	4
938	2
939	6
940	2
941	4
942	2
943	10
944	2
945	4
946	2
947	6
948	2
949	4
950	2
951	8
952	2
953	4
954	2
955	6
956	2
957	4
958	2
959	14
960	2
961	4
962	2
963	6
964	2
965	4
966	2
967	8
968	2
969	4
970	2
971	6
972	2
973	4
974	2
975	10
976	2
977	4
978	2
979	6
980	2
981	4
982	2
983	8
984	2
985	4
986	2
987	6
988	2
989	4
990	2
991	12
992	2
993	4
994	2
995	6
996	2
997	4
998	2
999	8
"""