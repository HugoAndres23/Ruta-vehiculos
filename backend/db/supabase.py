import time
from supabase import create_client, Client
from db import schemas
from core.security import get_password_hash, verify_password
from fastapi import HTTPException

url = "https://xiiunfoypbekcgtkwwra.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhpaXVuZm95cGJla2NndGt3d3JhIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc5Mjc5MjAsImV4cCI6MjAxMzUwMzkyMH0.c_ZhUEgX6O6xRQK2LO4csALUxweXQugmaXpK7HcXtjA"
supabase: Client = create_client(url, key)


def login(email, password):
    user = supabase.table("voters").select("*").eq("email", email).execute()
    if not user.data:
        return None
    if not verify_password(password, user.data[0]["hashed_password"]):
        return None
    return user.data[0]


def register_voter(voter_data: schemas.VoterCreate):
    try:
        new_voter, count = (
            supabase.table("voters")
            .insert(
                {
                    "first_name": voter_data.first_name,
                    "last_name": voter_data.last_name,
                    "email": voter_data.email,
                    "document_number": voter_data.document_number,
                    "date_birth": voter_data.date_birth,
                    "address": voter_data.address,
                    "hashed_password": get_password_hash(voter_data.password),
                }
            )
            .execute()
        )
        return new_voter

    except Exception as e:
        if "duplicate key value violates unique constraint" in str(e):
            raise HTTPException(status_code=400, detail="User already exist")
        else:
            return e


def register_vote(vote: schemas.VoteCreate):
    new_vote, count = (
        supabase.table("votes")
        .insert(
            {
                "id_voter": vote.id_voter,
                "id_candidate": vote.id_candidate,
                "id_candidature": vote.id_candidature,
            }
        )
        .execute()
    )
    return new_vote


def get_by_id(id: int):
    user = supabase.table("voters").select("*").eq("id", id).execute()
    if not user.data:
        return None
    return user.data[0]


def get_candidatures():
    candidatures = supabase.table("candidatures").select("*").execute()
    if not candidatures.data:
        return candidatures.data.append("Candidatura no encontrada")
    return candidatures.data


def get_candidates(candidatura: int):
    candidates = (
        supabase.table("candidates")
        .select("*")
        .eq("candidature", candidatura)
        .execute()
    )
    if not candidates.data:
        return candidates.data.append("Candidatos no encontrados")
    return candidates.data


def get_candidate_by_id(id: int):
    candidate = supabase.table("candidates").select("id").eq("id", id).execute()
    if not candidate.data:
        return candidate.data.append("Candidato no encontrado")
    return candidate.data[0]


def get_votes_by_candidature(candidatura: int):
    votes = (
        supabase.table("votes").select("*").eq("id_candidature", candidatura).execute()
    )
    if not votes.data:
        return votes.data.append("Votos no encontrados")
    return votes.data


def already_voted(voter_id: int, candidature_id: int):
    vote = (
        supabase.table("votes")
        .select("*")
        .eq("id_voter", voter_id)
        .eq("id_candidature", candidature_id)
        .execute()
    )
    if not vote.data:
        return False
    return True
