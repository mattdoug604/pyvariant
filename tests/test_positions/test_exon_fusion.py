import pytest

from variant_map.constants import FUSION
from variant_map.positions import (
    CdnaFusion,
    CdnaPosition,
    DnaFusion,
    DnaPosition,
    ExonFusion,
    ExonPosition,
    ProteinFusion,
    ProteinPosition,
    RnaFusion,
    RnaPosition,
)


@pytest.fixture()
def variant():
    breakpoint1 = ExonPosition(
        contig_id="X",
        start=3,
        start_offset=0,
        end=4,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000068323",
        gene_name="TFE3",
        transcript_id="ENST00000315869",
        transcript_name="TFE3-001",
        exon_id="ENSE00002939607",
    )
    breakpoint2 = ExonPosition(
        contig_id="1",
        start=2,
        start_offset=0,
        end=2,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000143294",
        gene_name="PRCC",
        transcript_id="ENST00000271526",
        transcript_name="PRCC-001",
        exon_id="ENSE00002871917",
    )
    return ExonFusion(breakpoint1, breakpoint2)


def test_str(variant):
    assert str(variant) == "ENST00000315869:e.3_4::ENST00000271526:e.2"


def test_type(variant):
    assert not variant.is_cdna
    assert not variant.is_dna
    assert variant.is_exon
    assert not variant.is_protein
    assert not variant.is_rna


def test_variant_type(variant):
    assert variant.variant_type == FUSION
    assert not variant.is_deletion
    assert not variant.is_delins
    assert not variant.is_duplication
    assert not variant.is_frameshift
    assert variant.is_fusion
    assert not variant.is_insertion
    assert not variant.is_substitution


def test_to_cdna(ensembl69, variant):
    breakpoint1 = CdnaPosition(
        contig_id="X",
        start=231,
        start_offset=0,
        end=780,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000068323",
        gene_name="TFE3",
        transcript_id="ENST00000315869",
        transcript_name="TFE3-001",
        protein_id="ENSP00000314129",
    )
    breakpoint2 = CdnaPosition(
        contig_id="1",
        start=469,
        start_offset=0,
        end=516,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000143294",
        gene_name="PRCC",
        transcript_id="ENST00000271526",
        transcript_name="PRCC-001",
        protein_id="ENSP00000271526",
    )
    expected = [CdnaFusion(breakpoint1, breakpoint2)]
    assert ensembl69.to_cdna(variant) == expected


def test_to_dna(ensembl69, variant):
    breakpoint1 = DnaPosition(
        contig_id="X", start=48895722, start_offset=0, end=48896935, end_offset=0, strand="-"
    )
    breakpoint2 = DnaPosition(
        contig_id="1", start=156752074, start_offset=0, end=156752121, end_offset=0, strand="+"
    )
    expected = [DnaFusion(breakpoint1, breakpoint2)]
    assert ensembl69.to_dna(variant) == expected


def test_to_exon(ensembl69, variant):
    breakpoint1 = ExonPosition(
        contig_id="X",
        start=3,
        start_offset=0,
        end=4,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000068323",
        gene_name="TFE3",
        transcript_id="ENST00000315869",
        transcript_name="TFE3-001",
        exon_id="ENSE00002939607",
    )
    breakpoint2 = ExonPosition(
        contig_id="1",
        start=2,
        start_offset=0,
        end=2,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000143294",
        gene_name="PRCC",
        transcript_id="ENST00000271526",
        transcript_name="PRCC-001",
        exon_id="ENSE00002871917",
    )
    expected = [ExonFusion(breakpoint1, breakpoint2)]
    assert ensembl69.to_exon(variant) == expected


def test_to_protein(ensembl69, variant):
    breakpoint1 = ProteinPosition(
        contig_id="X",
        start=77,
        start_offset=0,
        end=260,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000068323",
        gene_name="TFE3",
        transcript_id="ENST00000315869",
        transcript_name="TFE3-001",
        protein_id="ENSP00000314129",
    )
    breakpoint2 = ProteinPosition(
        contig_id="1",
        start=157,
        start_offset=0,
        end=172,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000143294",
        gene_name="PRCC",
        transcript_id="ENST00000271526",
        transcript_name="PRCC-001",
        protein_id="ENSP00000271526",
    )
    expected = [ProteinFusion(breakpoint1, breakpoint2)]
    assert ensembl69.to_protein(variant) == expected


def test_to_rna(ensembl69, variant):
    breakpoint1 = RnaPosition(
        contig_id="X",
        start=491,
        start_offset=0,
        end=1040,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000068323",
        gene_name="TFE3",
        transcript_id="ENST00000315869",
        transcript_name="TFE3-001",
    )
    breakpoint2 = RnaPosition(
        contig_id="1",
        start=741,
        start_offset=0,
        end=788,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000143294",
        gene_name="PRCC",
        transcript_id="ENST00000271526",
        transcript_name="PRCC-001",
    )
    expected = [RnaFusion(breakpoint1, breakpoint2)]
    assert ensembl69.to_rna(variant) == expected
