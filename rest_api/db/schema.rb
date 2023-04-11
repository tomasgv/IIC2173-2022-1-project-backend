# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2022_06_26_054853) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "pgcrypto"
  enable_extension "plpgsql"
  enable_extension "postgis"
  enable_extension "uuid-ossp"

  create_table "locations", force: :cascade do |t|
    t.bigint "user_id"
    t.string "name"
    t.geography "lonlat", limit: {:srid=>4326, :type=>"st_point", :geographic=>true}
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "temp"
    t.index ["user_id"], name: "index_locations_on_user_id"
  end

  create_table "locations_tags", id: false, force: :cascade do |t|
    t.bigint "location_id"
    t.bigint "tag_id"
    t.index ["location_id"], name: "index_locations_tags_on_location_id"
    t.index ["tag_id"], name: "index_locations_tags_on_tag_id"
  end

  create_table "pings", force: :cascade do |t|
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "sender_id"
    t.bigint "recipient_id"
    t.float "sidi_index"
    t.float "siin_index"
    t.float "dindin_index"
    t.boolean "accepted"
    t.boolean "livetracker"
  end

  create_table "tags", force: :cascade do |t|
    t.string "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "users", force: :cascade do |t|
    t.string "name"
    t.string "email"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "nickname"
    t.string "phone"
    t.uuid "uuid", default: -> { "uuid_generate_v4()" }, null: false
    t.uuid "entity_uuid", default: -> { "uuid_generate_v4()" }, null: false
    t.string "token"
  end

  create_table "users_tags", id: false, force: :cascade do |t|
    t.bigint "user_id"
    t.bigint "tag_id"
    t.index ["tag_id"], name: "index_users_tags_on_tag_id"
    t.index ["user_id"], name: "index_users_tags_on_user_id"
  end

end
