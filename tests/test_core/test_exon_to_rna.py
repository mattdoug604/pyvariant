from ensembl_map.core import ExonPosition, RnaPosition


def test_negative_strand(ensembl100):
    position = ExonPosition(
        _data=ensembl100,
        contig_id="5",
        start=2,
        end=2,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
        exon_id="ENSE00001197112",
    )
    expected = RnaPosition(
        _data=ensembl100,
        contig_id="5",
        start=299,
        end=1652,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
    )
    assert position.to_rna() == [expected]


def test_positive_strand(ensembl100):
    position = ExonPosition(
        _data=ensembl100,
        contig_id="13",
        start=3,
        end=3,
        strand="+",
        gene_id="ENSG00000139618",
        gene_name="BRCA2",
        transcript_id="ENST00000380152",
        transcript_name="BRCA2-201",
        exon_id="ENSE00003666217",
    )
    expected = RnaPosition(
        _data=ensembl100,
        contig_id="13",
        start=301,
        end=549,
        strand="+",
        gene_id="ENSG00000139618",
        gene_name="BRCA2",
        transcript_id="ENST00000380152",
        transcript_name="BRCA2-201",
    )
    assert position.to_rna() == [expected]