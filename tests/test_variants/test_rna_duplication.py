import pytest

from pyvariant.constants import DUPLICATION
from pyvariant.variants import CdnaDuplication, DnaDuplication, ProteinDuplication, RnaDuplication


@pytest.fixture()
def variant(ensembl69):
    return RnaDuplication(
        _core=ensembl69,
        contig_id="4",
        start=977,
        start_offset=0,
        end=979,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000157404",
        gene_name="KIT",
        transcript_id="ENST00000288135",
        transcript_name="KIT-001",
        refseq="AAT",
        altseq="AATAAT",
    )


def test_str(variant):
    assert str(variant) == "ENST00000288135:r.977_979dup"


def test_to_string_gene_name(variant):
    assert variant.to_string(reference="gene_name") == "KIT:r.977_979dup"


def test_type(variant):
    assert not variant.is_cdna
    assert not variant.is_dna
    assert not variant.is_exon
    assert not variant.is_protein
    assert variant.is_rna


def test_variant_type(variant):
    assert variant.variant_type == DUPLICATION
    assert not variant.is_deletion
    assert not variant.is_delins
    assert variant.is_duplication
    assert not variant.is_frameshift
    assert not variant.is_fusion
    assert not variant.is_insertion
    assert not variant.is_substitution


def test_to_cdna(ensembl69, variant):
    expected = [
        CdnaDuplication(
            _core=ensembl69,
            contig_id="4",
            start=880,
            start_offset=0,
            end=882,
            end_offset=0,
            strand="+",
            gene_id="ENSG00000157404",
            gene_name="KIT",
            transcript_id="ENST00000288135",
            transcript_name="KIT-001",
            protein_id="ENSP00000288135",
            refseq="AAT",
            altseq="AATAAT",
        )
    ]
    assert variant.to_cdna() == expected


def test_to_dna(ensembl69, variant):
    expected = [
        DnaDuplication(
            _core=ensembl69,
            contig_id="4",
            start=55570013,
            start_offset=0,
            end=55570015,
            end_offset=0,
            strand="+",
            refseq="AAT",
            altseq="AATAAT",
        )
    ]
    assert variant.to_dna() == expected


def test_to_protein(ensembl69, variant):
    expected = [
        ProteinDuplication(
            _core=ensembl69,
            contig_id="4",
            start=294,
            start_offset=0,
            end=294,
            end_offset=0,
            strand="+",
            gene_id="ENSG00000157404",
            gene_name="KIT",
            transcript_id="ENST00000288135",
            transcript_name="KIT-001",
            protein_id="ENSP00000288135",
            refseq="N",
            altseq="NN",
        )
    ]
    assert variant.to_protein() == expected


def test_to_rna(ensembl69, variant):
    expected = [
        RnaDuplication(
            _core=ensembl69,
            contig_id="4",
            start=977,
            start_offset=0,
            end=979,
            end_offset=0,
            strand="+",
            gene_id="ENSG00000157404",
            gene_name="KIT",
            transcript_id="ENST00000288135",
            transcript_name="KIT-001",
            refseq="AAT",
            altseq="AATAAT",
        )
    ]
    assert variant.to_rna() == expected
