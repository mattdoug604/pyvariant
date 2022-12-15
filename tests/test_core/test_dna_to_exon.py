from ensembl_map.core import DnaPosition, ExonPosition


def test_negative_strand(ensembl100):
    position = DnaPosition(_data=ensembl100, contig_id="5", start=1294864, end=1294866, strand="-")
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="5",
        start=1,
        end=1,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
        exon_id="ENSE00003896691",
    )
    assert expected in position.to_exon()


def test_negative_strand_cdna_protein_end(ensembl100):
    position = DnaPosition(_data=ensembl100, contig_id="5", start=1253728, end=1253730, strand="-")
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="5",
        start=16,
        end=16,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
        exon_id="ENSE00001863787",
    )
    assert expected in position.to_exon()


def test_negative_strand_cdna_protein_start(ensembl100):
    position = DnaPosition(_data=ensembl100, contig_id="5", start=1294987, end=1294989, strand="-")
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="5",
        start=1,
        end=1,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
        exon_id="ENSE00003896691",
    )
    assert expected in position.to_exon()


def test_negative_strand_overlapping_genes_different_strands(ensembl100):
    position = DnaPosition(
        _data=ensembl100, contig_id="6", start=31166302, end=31166304, strand="-"
    )
    expected = [
        ExonPosition(
            _data=ensembl100,
            contig_id="6",
            start=1,
            end=1,
            strand="-",
            gene_id="ENSG00000204531",
            gene_name="POU5F1",
            transcript_id="ENST00000471529",
            transcript_name="POU5F1-204",
            exon_id="ENSE00002568331",
        ),
        ExonPosition(
            _data=ensembl100,
            contig_id="6",
            start=1,
            end=1,
            strand="-",
            gene_id="ENSG00000204531",
            gene_name="POU5F1",
            transcript_id="ENST00000513407",
            transcript_name="POU5F1-206",
            exon_id="ENSE00002033137",
        ),
    ]
    assert position.to_exon() == expected


def test_negative_strand_transcript_end(ensembl100):
    position = DnaPosition(_data=ensembl100, contig_id="5", start=1253167, end=1253169, strand="-")
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="5",
        start=16,
        end=16,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
        exon_id="ENSE00001863787",
    )
    assert expected in position.to_exon()


def test_negative_strand_transcript_start(ensembl100):
    position = DnaPosition(_data=ensembl100, contig_id="5", start=1295066, end=1295068, strand="-")
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="5",
        start=1,
        end=1,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
        exon_id="ENSE00003896691",
    )
    assert expected in position.to_exon()


def test_positive_strand(ensembl100):
    position = DnaPosition(
        _data=ensembl100, contig_id="13", start=32371034, end=32371036, strand="+"
    )
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="13",
        start=20,
        end=20,
        strand="+",
        gene_id="ENSG00000139618",
        gene_name="BRCA2",
        transcript_id="ENST00000380152",
        transcript_name="BRCA2-201",
        exon_id="ENSE00000939180",
    )
    assert expected in position.to_exon()


def test_positive_strand_cdna_protein_end(ensembl100):
    position = DnaPosition(
        _data=ensembl100, contig_id="13", start=32398768, end=32398770, strand="+"
    )
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="13",
        start=27,
        end=27,
        strand="+",
        gene_id="ENSG00000139618",
        gene_name="BRCA2",
        transcript_id="ENST00000380152",
        transcript_name="BRCA2-201",
        exon_id="ENSE00003717596",
    )
    assert expected in position.to_exon()


def test_positive_strand_cdna_protein_start(ensembl100):
    position = DnaPosition(
        _data=ensembl100, contig_id="13", start=32316461, end=32316463, strand="+"
    )
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="13",
        start=2,
        end=2,
        strand="+",
        gene_id="ENSG00000139618",
        gene_name="BRCA2",
        transcript_id="ENST00000380152",
        transcript_name="BRCA2-201",
        exon_id="ENSE00001484009",
    )
    assert expected in position.to_exon()


def test_positive_strand_overlapping_genes_different_strands(ensembl100):
    position = DnaPosition(
        _data=ensembl100, contig_id="6", start=31166302, end=31166304, strand="+"
    )
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="6",
        start=2,
        end=2,
        strand="+",
        gene_id="ENSG00000137310",
        gene_name="TCF19",
        transcript_id="ENST00000542218",
        transcript_name="TCF19-204",
        exon_id="ENSE00002283659",
    )
    assert position.to_exon() == [expected]


def test_positive_strand_transcript_end(ensembl100):
    position = DnaPosition(
        _data=ensembl100, contig_id="13", start=32400264, end=32400266, strand="+"
    )
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="13",
        start=27,
        end=27,
        strand="+",
        gene_id="ENSG00000139618",
        gene_name="BRCA2",
        transcript_id="ENST00000380152",
        transcript_name="BRCA2-201",
        exon_id="ENSE00003717596",
    )
    assert expected in position.to_exon()


def test_positive_strand_transcript_start(ensembl100):
    position = DnaPosition(
        _data=ensembl100, contig_id="13", start=32315474, end=32315476, strand="+"
    )
    expected = ExonPosition(
        _data=ensembl100,
        contig_id="13",
        start=1,
        end=1,
        strand="+",
        gene_id="ENSG00000139618",
        gene_name="BRCA2",
        transcript_id="ENST00000380152",
        transcript_name="BRCA2-201",
        exon_id="ENSE00001184784",
    )
    assert expected in position.to_exon()