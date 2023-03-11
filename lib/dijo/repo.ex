defmodule Dijo.Repo do
  use Ecto.Repo,
    otp_app: :dijo,
    adapter: Ecto.Adapters.Postgres
end
