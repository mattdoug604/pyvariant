import pytest

from pyvariant.constants import DELINS
from pyvariant.variants import CdnaDelins, DnaDelins, ProteinDelins, RnaDelins


@pytest.fixture()
def variant(ensembl69):
    return ProteinDelins(
        _core=ensembl69,
        contig_id="4",
        start=417,
        start_offset=0,
        end=419,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000157404",
        gene_name="KIT",
        transcript_id="ENST00000288135",
        transcript_name="KIT-001",
        protein_id="ENSP00000288135",
        refseq="TYD",
        altseq="I",
    )


def test_str(variant):
    assert str(variant) == "ENSP00000288135:p.T417_D419delinsI"


def test_to_string_gene_name(variant):
    assert variant.to_string(reference="gene_name") == "KIT:p.T417_D419delinsI"


def test_type(variant):
    assert not variant.is_cdna
    assert not variant.is_dna
    assert not variant.is_exon
    assert variant.is_protein
    assert not variant.is_rna


def test_variant_type(variant):
    assert variant.variant_type == DELINS
    assert not variant.is_deletion
    assert variant.is_delins
    assert not variant.is_duplication
    assert not variant.is_frameshift
    assert not variant.is_fusion
    assert not variant.is_insertion
    assert not variant.is_substitution


def test_to_cdna(ensembl69, variant):
    expected = CdnaDelins(
        _core=ensembl69,
        contig_id="4",
        start=1250,
        start_offset=0,
        end=1257,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000157404",
        gene_name="KIT",
        transcript_id="ENST00000288135",
        transcript_name="KIT-001",
        protein_id="ENSP00000288135",
        refseq="CTTACGAC",
        altseq="TA",
    )
    result = variant.to_cdna()
    assert expected in result
    assert len(result) == 3


def test_to_dna(ensembl69, variant):
    expected = DnaDelins(
        _core=ensembl69,
        contig_id="4",
        start=55589768,
        start_offset=0,
        end=55589775,
        end_offset=0,
        strand="+",
        refseq="CTTACGAC",
        altseq="TA",
    )
    result = variant.to_dna()
    assert expected in result
    assert len(result) == 3


def test_to_protein(ensembl69, variant):
    expected = [
        ProteinDelins(
            _core=ensembl69,
            contig_id="4",
            start=417,
            start_offset=0,
            end=419,
            end_offset=0,
            strand="+",
            gene_id="ENSG00000157404",
            gene_name="KIT",
            transcript_id="ENST00000288135",
            transcript_name="KIT-001",
            protein_id="ENSP00000288135",
            refseq="TYD",
            altseq="I",
        )
    ]
    assert variant.to_protein() == expected


def test_to_rna(ensembl69, variant):
    expected = RnaDelins(
        _core=ensembl69,
        contig_id="4",
        start=1347,
        start_offset=0,
        end=1354,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000157404",
        gene_name="KIT",
        transcript_id="ENST00000288135",
        transcript_name="KIT-001",
        refseq="CTTACGAC",
        altseq="TA",
    )
    result = variant.to_rna()
    assert expected in result
    assert len(result) == 3
