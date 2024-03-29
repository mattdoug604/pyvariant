import pytest

from pyvariant.constants import FUSION
from pyvariant.variants import (
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
def variant(ensembl69):
    breakpoint1 = ProteinPosition(
        _core=ensembl69,
        contig_id="X",
        start=178,
        start_offset=0,
        end=182,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000068323",
        gene_name="TFE3",
        transcript_id="ENST00000315869",
        transcript_name="TFE3-001",
        protein_id="ENSP00000314129",
    )
    breakpoint2 = ProteinPosition(
        _core=ensembl69,
        contig_id="1",
        start=157,
        start_offset=0,
        end=160,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000143294",
        gene_name="PRCC",
        transcript_id="ENST00000271526",
        transcript_name="PRCC-001",
        protein_id="ENSP00000271526",
    )
    return ProteinFusion(ensembl69, breakpoint1, breakpoint2)


def test_str(variant):
    assert str(variant) == "ENSP00000314129:p.178_182::ENSP00000271526:p.157_160"


def test_to_string_gene_name(variant):
    assert variant.to_string(reference="gene_name") == "TFE3:p.178_182::PRCC:p.157_160"


def test_type(variant):
    assert not variant.is_cdna
    assert not variant.is_dna
    assert not variant.is_exon
    assert variant.is_protein
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
        _core=ensembl69,
        contig_id="X",
        start=532,
        start_offset=0,
        end=546,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000068323",
        gene_name="TFE3",
        transcript_id="ENST00000315869",
        transcript_name="TFE3-001",
        protein_id="ENSP00000314129",
    )
    breakpoint2 = CdnaPosition(
        _core=ensembl69,
        contig_id="1",
        start=469,
        start_offset=0,
        end=480,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000143294",
        gene_name="PRCC",
        transcript_id="ENST00000271526",
        transcript_name="PRCC-001",
        protein_id="ENSP00000271526",
    )
    expected = [CdnaFusion(ensembl69, breakpoint1, breakpoint2)]
    assert variant.to_cdna() == expected


def test_to_dna(ensembl69, variant):
    breakpoint1 = DnaPosition(
        _core=ensembl69,
        contig_id="X",
        start=48895956,
        start_offset=0,
        end=48896634,
        end_offset=0,
        strand="-",
    )
    breakpoint2 = DnaPosition(
        _core=ensembl69,
        contig_id="1",
        start=156752074,
        start_offset=0,
        end=156752085,
        end_offset=0,
        strand="+",
    )
    expected = [DnaFusion(ensembl69, breakpoint1, breakpoint2)]
    assert variant.to_dna() == expected


def test_to_exon(ensembl69, variant):
    breakpoint1 = ExonPosition(
        _core=ensembl69,
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
        _core=ensembl69,
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
    expected = [ExonFusion(ensembl69, breakpoint1, breakpoint2)]
    assert variant.to_exon() == expected


def test_to_protein(ensembl69, variant):
    breakpoint1 = ProteinPosition(
        _core=ensembl69,
        contig_id="X",
        start=178,
        start_offset=0,
        end=182,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000068323",
        gene_name="TFE3",
        transcript_id="ENST00000315869",
        transcript_name="TFE3-001",
        protein_id="ENSP00000314129",
    )
    breakpoint2 = ProteinPosition(
        _core=ensembl69,
        contig_id="1",
        start=157,
        start_offset=0,
        end=160,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000143294",
        gene_name="PRCC",
        transcript_id="ENST00000271526",
        transcript_name="PRCC-001",
        protein_id="ENSP00000271526",
    )
    expected = [ProteinFusion(ensembl69, breakpoint1, breakpoint2)]
    assert variant.to_protein() == expected


def test_to_rna(ensembl69, variant):
    breakpoint1 = RnaPosition(
        _core=ensembl69,
        contig_id="X",
        start=792,
        start_offset=0,
        end=806,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000068323",
        gene_name="TFE3",
        transcript_id="ENST00000315869",
        transcript_name="TFE3-001",
    )
    breakpoint2 = RnaPosition(
        _core=ensembl69,
        contig_id="1",
        start=741,
        start_offset=0,
        end=752,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000143294",
        gene_name="PRCC",
        transcript_id="ENST00000271526",
        transcript_name="PRCC-001",
    )
    expected = [RnaFusion(ensembl69, breakpoint1, breakpoint2)]
    assert variant.to_rna() == expected
