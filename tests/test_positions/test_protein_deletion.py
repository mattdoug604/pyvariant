import pytest

from variant_map.constants import DELETION
from variant_map.positions import CdnaDeletion, DnaDeletion, ProteinDeletion, RnaDeletion


@pytest.fixture()
def variant():
    return ProteinDeletion(
        contig_id="10",
        start=632,
        start_offset=0,
        end=633,
        end_offset=0,
        gene_id="ENSG00000165731",
        gene_name="RET",
        transcript_id="ENST00000340058",
        transcript_name="RET-002",
        protein_id="ENSP00000344798",
        strand="+",
        refseq="EL",
        altseq="",
    )


def test_str(variant):
    assert str(variant) == "ENSP00000344798:p.E632_L633del"


def test_type(variant):
    assert not variant.is_cdna
    assert not variant.is_dna
    assert not variant.is_exon
    assert variant.is_protein
    assert not variant.is_rna


def test_variant_type(variant):
    assert variant.variant_type == DELETION
    assert variant.is_deletion
    assert not variant.is_delins
    assert not variant.is_duplication
    assert not variant.is_frameshift
    assert not variant.is_fusion
    assert not variant.is_insertion
    assert not variant.is_substitution


def test_to_cdna(ensembl69, variant):
    expected = [
        CdnaDeletion(
            contig_id="10",
            start=1894,
            start_offset=0,
            end=1899,
            end_offset=0,
            gene_id="ENSG00000165731",
            gene_name="RET",
            transcript_id="ENST00000340058",
            transcript_name="RET-002",
            protein_id="ENSP00000344798",
            strand="+",
            refseq="GAGCTG",
            altseq="",
        )
    ]
    assert ensembl69.to_cdna(variant) == expected


def test_to_dna(ensembl69, variant):
    expected = [
        DnaDeletion(
            contig_id="10",
            start=43609942,
            start_offset=0,
            end=43609947,
            end_offset=0,
            strand="+",
            refseq="GAGCTG",
            altseq="",
        )
    ]
    assert ensembl69.to_dna(variant) == expected


def test_to_protein(ensembl69, variant):
    expected = [
        ProteinDeletion(
            contig_id="10",
            start=632,
            start_offset=0,
            end=633,
            end_offset=0,
            strand="+",
            gene_id="ENSG00000165731",
            gene_name="RET",
            transcript_id="ENST00000340058",
            transcript_name="RET-002",
            protein_id="ENSP00000344798",
            refseq="EL",
            altseq="",
        )
    ]
    assert ensembl69.to_protein(variant) == expected


def test_to_rna(ensembl69, variant):
    expected = [
        RnaDeletion(
            contig_id="10",
            start=2074,
            start_offset=0,
            end=2079,
            end_offset=0,
            strand="+",
            gene_id="ENSG00000165731",
            gene_name="RET",
            transcript_id="ENST00000340058",
            transcript_name="RET-002",
            refseq="GAGCTG",
            altseq="",
        )
    ]
    assert ensembl69.to_rna(variant) == expected
